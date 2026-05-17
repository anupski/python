import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

#------------------------------------------------------------------------------------------------------

import requests
res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
print(res.status_code)
print(res.content)

#------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())

#------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.w3schools.com/python/module_requests.asp')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())

#------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.python.org/downloads/')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())

#--------------------------------------------------------------------------------------------------------

import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pydantic import BaseModel


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
res = requests.get('https://www.python.org/downloads/', headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

class PythonRelease(BaseModel):
    version: str
    release_date: str
    download_link: str
    
scraped_data = [] 


release_container = soup.find('div', class_='download-list-widget')

if release_container:
    
    for row in release_container.find_all('li'): 
        
        version_element = row.find('span', class_='release-number')
        date_element = row.find('span', class_='release-date')
        
        if version_element and date_element:
            
            version_text = version_element.text.strip()
            date_text = date_element.text.strip()
            
            
            link_tag = version_element.find('a')
            if link_tag and 'href' in link_tag.attrs:
                url = link_tag['href']
                full_url = url if url.startswith('http') else f"https://www.python.org{url}"
                
                try:
                    release = PythonRelease(
                        version=version_text, 
                        release_date=date_text,
                        download_link=full_url
                    )
                    scraped_data.append(release.model_dump()) 
                except Exception as e:
                    print(f"Validation Error: {e}")
else:
    print("Could not find the release container element on the page.")


if scraped_data:
    json_output = json.dumps(scraped_data, indent=4)
    print("--- JSON OUTPUT ---")
    print(json_output[:500]) 

    df = pd.DataFrame(scraped_data)
    print("\n--- PANDAS DATAFRAME OUTPUT ---")
    print(df.head())

    df.to_csv('python_releases.csv', index=False)
    print("\n Success! 'python_releases.csv' has been created with data.")
else:
    print("\n No data was scraped. Check if the website layout changed.")
