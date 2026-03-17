# import requests
from lxml import html, etree
import os
from parse_using_xpath import xpath_data


## get html content using url

# def read_html_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }
#     response = requests.get(url, headers=headers)
#     tree = html.fromstring(response.text)

#     # convert to formatted HTML
#     formatted_html = etree.tostring(tree, pretty_print=True, encoding="unicode")
#     with open("wendys_html_content.html", "w", encoding="utf-8") as f:
#         f.write(formatted_html)
#     return formatted_html


## get html content using direct file

def read_html_content(file_name):
    current_working_dir = os.getcwd()
    file_path = f"{current_working_dir}/{file_name}"
    with open(file_path, "r", encoding='utf-8') as f :
        html_content = f.read()
    return html_content

def extract_data_from_html(html_content):
    product_list = []
    dict_data = {}
    tree = html.fromstring(html_content)
    categoies_info_data = tree.xpath(xpath_data.get("categoies_base_path"))
    print(len(categoies_info_data))
    count = 0
    for single_element in categoies_info_data:
        dict_data = {}
        dict_data["product_name"] = single_element.xpath(xpath_data.get("product_name"))

        count_value = single_element.xpath(xpath_data.get("product_count")).replace("(", "").replace(")", "")
        dict_data["product_count"] = count_value if count_value else 0
        
        dict_data["product_image"] = single_element.xpath(xpath_data.get("product_image"))
        
        product_list.append(dict_data)
    print(product_list[0])
    print(len(product_list))
    return product_list
