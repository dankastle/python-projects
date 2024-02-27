
import requests
from bs4 import BeautifulSoup


response = requests.get('http://www.wisdompetmed.com/')
print ((response).text)

soup = BeautifulSoup(response.text)

print(soup.find("span", class_ = "phone").text)

# write HTML code we pulled to a text file
with open ("wisdom_pet.txt", "w") as f:
  f.write(soup.prettify())

# capture only the scraped links for the site to a file
links = soup.find_all("a")
with open("wisdom_pet_links.txt", "w") as l:
    for link in links:
        l.write(f"{link.text} - {link.get('href')}\n")
