import requests
from bs4 import BeautifulSoup
def main():
	url = 'https://www.zwilling.com/us/search/?q=40508-614'
	result = requests.get(url)
	src = result.content
	soup = BeautifulSoup(src,'lxml')
	print(soup.title.string)
	

if __name__ == "__main__":
	main()
