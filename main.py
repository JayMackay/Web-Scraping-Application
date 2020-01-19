#Imported libraries and funcctions
from urllib.request import urlopen as uReq #Grab requested webpage URL
from bs4 import BeautifulSoup as soup #Parse HTML text into a specified format

#Specifed webpage URL to scrape data
my_url = 'https://www.newegg.com/global/uk-en/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#Inititalizing connection, grabbing the webpage
uClient = uReq(my_url)
page_html = uClient.read() #Offload the content into a variable
uClient.close() #Close the client

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Find all division elements with the class object "item-container"
containers = page_soup.findAll("div", {"class":"item-container"})
