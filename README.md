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
   git clone https://github.com/<your-org>/<your-repo>.git
   cd <your-repo>
