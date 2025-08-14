import os
import csv
import requests
from tqdm import tqdm

# --- Configuration ---
API_TOKEN = os.environ.get('SNYK_API_TOKEN')
GROUP_ID = os.environ.get('SNYK_GROUP_ID')
API_BASE_URL = 'https://api.snyk.io/rest'

if not API_TOKEN or not GROUP_ID:
    raise ValueError("Missing required environment variables: SNYK_API_TOKEN or SNYK_GROUP_ID.")

HEADERS = {
    'Authorization': f'Token {API_TOKEN}',
    'Content-Type': 'application/vnd.api+json',
    'Accept': 'application/vnd.api+json'
}


def fetch_all_pages(url):
    """Retrieve all results from a paginated Snyk API endpoint."""
    results = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        results.extend(data.get('data', []))
        url = data.get('links', {}).get('next')
    return results


def get_orgs_in_group(group_id):
    """Retrieve all organizations within a specified Snyk group."""
    return fetch_all_pages(f"{API_BASE_URL}/groups/{group_id}/orgs")


def get_projects_in_org(org_id):
    """Retrieve all projects within a specified Snyk organization."""
    return fetch_all_pages(f"{API_BASE_URL}/orgs/{org_id}/projects")


def main():
    output_file = "snyk_orgs_projects.csv"
    organizations = get_orgs_in_group(GROUP_ID)
    print(f"\n[INFO] Found {len(organizations)} organizations in the group.")

    total_projects = 0

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Organization ID", "Organization Name", "Project ID", "Project Name"])
        
        for org in tqdm(organizations, desc="Processing Organizations", unit="org"):
            org_id = org['id']
            org_name = org['attributes']['name']

            projects = get_projects_in_org(org_id)
            total_projects += len(projects)

            for p in projects:
                project_id = p['id']
                project_name = p['attributes']['name']
                writer.writerow([org_id, org_name, project_id, project_name])
                
    print(f"\n[INFO] Data successfully exported to '{output_file}'.")
    print(f"[INFO] Total projects found: {total_projects}")


if __name__ == "__main__":
    main()
