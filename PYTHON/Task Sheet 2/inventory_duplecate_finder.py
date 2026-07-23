# Inventory Duplicate Finder
print("---- Inventory Duplicate Finder -----")
product_codes = ["M8956","C1512","G6978","C1512","C1512","H0473","C1512 ","S7467","C1512"]
print("Original Product Codes:", product_codes)

# counting duplcate product_codes using count() method
duplicate_count = product_codes.count("C1512")
print(f"Duplicate count of 'C1512': {duplicate_count}")

# finding the index of the first occurrence of a product code using index() method
first_index = product_codes.index("C1512")   
print(f"First occurrence of 'C1512' is at index: {first_index}") 