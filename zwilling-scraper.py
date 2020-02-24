import requests
import pandas
from bs4 import BeautifulSoup

def main():
	#64085-200  category page example

	df = pandas.read_excel(r'D:\Github\test.xlsx')
	products = df[df.columns[0]].tolist()

	for product in products:
		url = 'https://www.zwilling.com/us/search/?q=' + str(product)
		result = requests.get(url)
		src = result.content
		soup = BeautifulSoup(src,'lxml')
		if is_product(soup.title.string):
			# find_name(soup)
			# find_price(soup)
			# find_copy(soup)
			find_details(soup)
	return

def check(tag):
	return tag is None

def import_product_list(self):
	#accept exel sheet and store valaues in list
	return

def is_product(title):
	if "Search results for" not in title:
		return True
	else:
		return False

def find_images(self):
	#return number of images on product page
	return

def find_details(soup):
	tag = soup.find(attrs={"class": "tab active"})
	if check(tag): return('empty')
	#find list and extract items
	return

def find_copy(soup):
	tag = soup.find(attrs={"class": "product-info-shortDescription"})
	if check(tag): return('empty')
	copy = tag.string
	print(copy)
	return copy

def find_price(soup):
	tag = soup.find(attrs={"class": "product-sales-price price-sales"})
	if check(tag): return('empty')
	price = tag.string
	print(price)
	return price

def find_characteristics(self):
	#return characteristics
	return

def find_measurements(self):
	#return measuremnts
	return

def find_name(soup):
	tag1 = soup.find(attrs={"class": "brand-name"})
	tag2 = soup.find(attrs={"class": "product-name"})
	name = tag1.string + ' ' + tag2.string
	print(name)
	return name

if __name__ == "__main__":
	main()