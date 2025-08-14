import os
import csv
import requests
from tqdm import tqdm

# --- Configuration ---
API_TOKEN = os.environ.get('SNYK_API_TOKEN')
GROUP_ID = os.environ.get('SNYK_GROUP_ID')
API_HOST = 'https://api.snyk.io'
API_BASE_URL = f'{API_HOST}/rest'
API_VERSION = '2024-07-29'

if not API_TOKEN:
    raise ValueError("Missing required environment variable: SNYK_API_TOKEN.")

HEADERS = {
    'Authorization': f'Token {API_TOKEN}',
    'Accept': 'application/vnd.api+json',
}

# --- Helper Functions ---

def fetch_all_pages(url):
    """Retrieve all results from a paginated Snyk API endpoint."""
    results = []
    paginated_url = f"{url}?version={API_VERSION}"
    
    while paginated_url:
        try:
            with requests.Session() as session:
                session.headers.update(HEADERS)
                response = session.get(paginated_url)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
            break

        if response.status_code >= 400:
            print(f"[ERROR] API request failed: {response.status_code} {response.text}")
            break

        try:
            data = response.json()
        except ValueError:
            print(f"[ERROR] Invalid JSON returned from {paginated_url}")
            break

        results.extend(data.get('data', []))
        
        # Handle pagination
        next_link = data.get('links', {}).get('next')
        if next_link:
            paginated_url = f"{API_HOST}{next_link}" if next_link.startswith('/') else next_link
        else:
            paginated_url = None
            
    return results

def get_orgs_in_group(group_id):
    """Fetch organizations in a group, fallback to org-level if group not found."""
    if group_id:
        orgs = fetch_all_pages(f"{API_BASE_URL}/groups/{group_id}/orgs")
        if orgs:
            return orgs
    return fetch_all_pages(f"{API_BASE_URL}/orgs")

def get_projects_in_org(org_id):
    """Retrieve all projects within an organization."""
    return fetch_all_pages(f"{API_BASE_URL}/orgs/{org_id}/projects")

# --- Main Script ---

def main():
    output_file = "snyk_orgs_projects.csv"
    organizations = get_orgs_in_group(GROUP_ID)
    print(f"\n[INFO] Found {len(organizations)} organizations.")

    total_projects = 0

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Modified header row
        writer.writerow(["Organization ID", "Organization Name", "Project ID", "Project Name"])

        for org in tqdm(organizations, desc="Processing Organizations", unit="org", leave=False):
            org_id = org['id']
            org_name = org['attributes'].get('name', 'Unknown')

            projects = get_projects_in_org(org_id)
            total_projects += len(projects)

            for p in projects:
                project_id = p['id']
                attributes = p.get('attributes', {})
                project_name = attributes.get('name', 'Unknown')
                
                # Modified data row to write
                writer.writerow([org_id, org_name, project_id, project_name])

    print(f"\n[INFO] Data successfully exported to '{output_file}'.")
    print(f"[INFO] Total projects found: {total_projects}")

if __name__ == "__main__":
    main()
