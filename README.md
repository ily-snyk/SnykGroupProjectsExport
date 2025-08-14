# getallprojects

Snyk Group Projects Export

This script retrieves all organizations in a specified Snyk group and exports their projects to a CSV file.
It uses the Snyk REST API and supports pagination to ensure all results are captured.

📋 Requirements

Python 3.8+

A Snyk API token with permission to read group and organization data

The Group ID for the Snyk group you want to query

📦 Installation

Clone this repository:

git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>


Install dependencies:

pip install -r requirements.txt


Requirements file example:

requests
tqdm

⚙️ Configuration

Set the required environment variables before running the script:

export SNYK_API_TOKEN="your_snyk_api_token"
export SNYK_GROUP_ID="your_snyk_group_id"

▶️ Usage

Run the script with:

python snyk_orgs_projects.py

📄 Output

The script creates a CSV file in the current directory:

snyk_orgs_projects.csv

Columns:

Organization ID

Organization Name

Project ID

Project Name

📝 Example Output
Organization ID,Organization Name,Project ID,Project Name
12345678-abcd-efgh-ijkl-1234567890ab,Example Org,abcd1234,example-project
12345678-abcd-efgh-ijkl-1234567890ab,Example Org,abcd5678,another-project

ℹ️ Notes

The script uses a progress bar to track progress while retrieving organizations and projects.

If your Snyk group contains a large number of projects, the script may take several minutes to complete.
