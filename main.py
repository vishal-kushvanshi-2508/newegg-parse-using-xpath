
from extract_data import *
import time
from store_data_database import *


file_name = "Computer parts, laptops, electronics, and more - Newegg United States.html"

def main():
    create_table()
    print("table and db create")
    html_content = read_html_content(file_name)
    product_list = extract_data_from_html(html_content)
    insert_data_in_table(list_data=product_list)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("time different  : ", end - start)





