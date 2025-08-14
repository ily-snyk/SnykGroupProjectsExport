# Snyk Group Projects Export

This script retrieves all organizations in a specified **Snyk group** and exports their projects to a CSV file.  
It uses the [Snyk REST API](https://apidocs.snyk.io/) and supports pagination to ensure all results are captured.

---

## 📋 Requirements

- Python **3.8+**
- A **Snyk API token** with permission to read group and organization data
- The **Group ID** for the Snyk group you want to query

---

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/ily-snyk/SnykGroupProjectsExport.git
   cd SnykGroupProjectsExport

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

 3. **Configuration:**
Set the required environment variables before running the script:
   ```bash
export SNYK_API_TOKEN="your_snyk_api_token"
export SNYK_GROUP_ID="your_snyk_group_id"

 4. **Usage:**
Run the script with:
   ```bash
python snyk_orgs_projects.py

📄 Output

The script creates a CSV file in the current directory:
snyk_orgs_projects.csv

Columns:
* Organization ID
* Organization Name
* Project ID
* Project Name
