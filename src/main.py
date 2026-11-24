import csv
from pathlib import Path

from database import get_products
from api_client import fetch_products


REPORT_PATH = Path(__file__).parent.parent / "data" / "reconciliation_report.csv"


def compare_products(local_products, api_products):
    local_names = {product["product_name"] for product in local_products}
    api_names = {product["title"] for product in api_products}

    only_in_local = local_names - api_names
    only_in_api = api_names - local_names
    common_products = local_names & api_names

    report_rows = []

    for product in local_products:
        report_rows.append({
            "product_name": product["product_name"],
            "source_system": "Local Database",
            "price": product["unit_price"],
            "status": "Only in Local Database"
        })

    for product in api_products:
        report_rows.append({
            "product_name": product["title"],
            "source_system": "External API",
            "price": product["price"],
            "status": "Only in External API"
        })

    for row in report_rows:
        if row["product_name"] in common_products:
            row["status"] = "Found in Both Systems"

    with open(REPORT_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["product_name", "source_system", "price", "status"]
        )
        writer.writeheader()
        writer.writerows(report_rows)

    print("\n--- RECONCILIATION REPORT ---")
    print(f"Local products: {len(local_products)}")
    print(f"API products: {len(api_products)}")
    print(f"Matching products: {len(common_products)}")
    print(f"Only in local database: {len(only_in_local)}")
    print(f"Only in API: {len(only_in_api)}")
    print(f"\nCSV report saved to: {REPORT_PATH}")


def main():
    local_products = get_products()
    api_products = fetch_products()

    compare_products(local_products, api_products)


if __name__ == "__main__":
    main()