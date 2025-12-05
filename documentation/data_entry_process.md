# Data Entry Process

## Task 1 – Customer List Cleanup

1. Copied the raw customer list from `datasets/raw/customers_raw.txt`.
2. Identified the key fields needed: full name, email, and phone number.
3. Removed extra spaces and unified separators (commas, dashes, pipes).
4. Standardized name capitalization (first letter uppercase, remaining lowercase).
5. Verified that each row had a valid email and phone format.
6. Saved the final table as `datasets/clean/customers_clean.csv`.

## Task 2 – Product Catalog Entry

1. Copied the raw product list from `datasets/raw/products_raw.txt`.
2. Defined consistent columns: product_name, category, price_usd.
3. Cleaned category names to be consistent (Electronics, Furniture).
4. Ensured all prices were numeric and in the same currency.
5. Saved the final table as `datasets/clean/products_clean.csv`.
