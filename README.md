# TechStore Integration Pipeline

## Overview
A Python-based system integration project that connects a local SQLite database with an external REST API, retrieves product data from both systems, compares datasets, and generates a reconciliation report.

The project simulates a common enterprise integration scenario in which data from different systems needs to be extracted, compared, and reconciled to identify inconsistencies.

## Business Objective
The goal is to demonstrate a basic data integration workflow between two independent data sources and identify discrepancies between their product catalogs.

The pipeline:
- Extracts product data from a local database.
- Retrieves product data from an external REST API.
- Compares records across the two systems.
- Identifies matching and unmatched products.
- Generates a CSV reconciliation report.

## Architecture

Local System (SQLite Database) + External System (REST API) → Python Integration Pipeline → Data Reconciliation → CSV Report

## Technologies Used
- Python
- SQLite
- REST API
- Requests
- SQL
- CSV
- Pytest

## Project Structure

```text
techstore-integration/
├── data/
│   ├── techstore.db
│   └── reconciliation_report.csv
├── src/
│   ├── api_client.py
│   ├── database.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

## Integration Workflow

1. Connect to the local SQLite database.
2. Retrieve product records from the database.
3. Fetch product records from the external Fake Store API.
4. Compare product names between the two data sources.
5. Identify:
   - Products available only in the local database.
   - Products available only in the external API.
   - Products present in both systems.
6. Generate a CSV reconciliation report.

## Reconciliation Results

During the initial execution:

| Data Source | Products Retrieved |
|---|---:|
| Local SQLite Database | 15 |
| External API | 20 |
| Matching Products | 0 |
| Products Only in Local Database | 15 |
| Products Only in API | 20 |

The absence of matching products reflects the different product catalogs used by the two data sources.

## Report Output

The pipeline automatically generates:

`data/reconciliation_report.csv`

The report includes:
- Product name
- Source system
- Product price
- Reconciliation status

## Automated Testing

The project includes automated tests using Pytest to validate the comparison logic under different scenarios:

- Products partially matching between systems.
- No matching products.
- All products matching.

Test execution:

```bash
pytest
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the integration pipeline

```bash
python src/main.py
```

### 4. Run tests

```bash
pytest
```

## Future Improvements

- Match products using identifiers and