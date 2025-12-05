import csv
from pathlib import Path

# Define paths for raw and clean datasets using pathlib for better path handling
RAW_DIR = Path("datasets/raw")
# Ensure the raw directory exists before reading files (may want to create it manually and add raw files)
CLEAN_DIR = Path("datasets/clean")
# Ensure the clean directory exists before writing files (created if not existing)
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

def clean_name(name: str) -> str:
    """Capitalize each part of the name properly."""
    return " ".join(part.capitalize() for part in name.split())

def clean_customers():
    """
    Read the raw customer list, clean it, and save a structured CSV file.
    This function:
    - Handles different separators (comma, dash, pipe, extra spaces)
    - Normalizes name capitalization
    - Ensures each row has name, email, and phone
    """
    input_file = RAW_DIR / "customers_raw.txt"
    output_file = CLEAN_DIR / "customers_clean.csv"

    rows = []
    with input_file.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                # Skip completely empty lines
                continue

            # Replace different separators ("|", "-", double spaces) with a comma, so we can split consistently
            for sep in ["|", "-", "  "]:
                line = line.replace(sep, ",")
            parts = [p.strip() for p in line.split(",") if p.strip()]

            if len(parts) < 3:
                # # If there is no name, email, phone, skip this line
                continue

            full_name = clean_name(parts[0])
            email = parts[1].lower()
            phone = parts[2]

            rows.append({
                "full_name": full_name,
                "email": email,
                "phone": phone
            })
    
    # Write the cleaned customer data into a CSV file with proper headers
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["full_name", "email", "phone"])
        writer.writeheader()
        writer.writerows(rows)

def clean_products():
    """
    Read the raw product list, clean it, and save a structured CSV file.
    This function:
    - Handles different separators
    - Extracts product name, category, and price
    - Standardizes category names and keeps prices numeric
    """
    input_file = RAW_DIR / "products_raw.txt"
    output_file = CLEAN_DIR / "products_clean.csv"

    rows = []
    with input_file.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                # Skip empty lines
                continue

            # # Replace different separators with a comma
            for sep in ["|", "-", "  "]:
                line = line.replace(sep, ",")
            parts = [p.strip() for p in line.split(",") if p.strip()]

            if len(parts) < 3:
                # Need at least product name, category, and price
                continue

            product_name = parts[0]
            
            # Detect which value is the price vs. the category.
            # Assumption: the first numeric-looking value is the price,
            # and the first non-numeric value is the category.
            price = None
            category = None
            for p in parts[1:]:
                try:
                    float(p)    # If this works, we treat it as price
                    price = p
                except ValueError:
                    if category is None:
                        category = p    # First non-numeric becomes the category

            if price is None or category is None:
                # If we couldn't reliably find both, skip that line
                continue
            
            # Standardize category name capitalization (i.e., 'electronics' to 'Electronics')
            category = category.capitalize()

            rows.append({
                "product_name": product_name,
                "category": category,
                "price_usd": price
            })
    
    # Write the cleaned product data into a CSV file with proper headers
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product_name", "category", "price_usd"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    # Run both cleaning functions when the script is executed
    clean_customers()
    clean_products()
    # Notify user of completion
    print("Cleaning complete. Check datasets/clean for output CSV files.")
