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

#Initialize CSV file to store extracted data
out_filename = "graphics_cards.csv"

#Header of CSV file to be written
headers = "brand, product_name, shipping \n"

#Opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

#For loops to grab attributes for each product
for container in containers:
   
    #Find all hyperlink elements within the first division
    make_rating_sp = container.div.select("a")

    #Grab the title from the image title attribute
    brand = make_rating_sp[0].img["title"].title()

    #Grab the text within the second "a" tag from within the list of queries
    product_name = container.div.select("a")[2].text

    #Find all list elements with the class "price-ship"
    #Clean the text of white space with strip()
    #Clean the strip of "Shipping $" if it exists to just get number
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    #Prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    #Writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", " ") + ", " + shipping + "\n")

f.close() 