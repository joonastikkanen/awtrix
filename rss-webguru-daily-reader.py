import requests
import xml.etree.ElementTree as ET
import logging
import json
import re
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def loadRSS():
  url = 'https://www.webcal.guru/fi-FI/rss'
  logging.info(f"Fetching RSS feed from {url}")
  resp = requests.get(url)
  with open('webcal-guru-today.xml', 'wb') as f:
    f.write(resp.content)
  logging.info("RSS feed saved to webcal-guru-today.xml")

def parseXML(xmlfile):
  logging.info(f"Parsing XML file {xmlfile}")
  tree = ET.parse(xmlfile)
  root = tree.getroot()
  titleitems = []
  for item in root.findall('./channel/item'):
    title = {}
    
    # iterate child elements of item 
    for child in item: 

        # special checking for namespace object content:media 
        if child.tag == '{http://search.yahoo.com/mrss/}content': 
            title['media'] = child.attrib['url'] 
        else: 
            title[child.tag] = child.text.encode('utf8') 
    titleitems.append(title)
  logging.info(f"Parsed {len(titleitems)} items from XML")
  return titleitems

def savetoJSON(titleitems, filename):
  logging.info(f"Saving {len(titleitems)} items to JSON file {filename}")
  filtered_items = []
  specific_titles = [
    'Title1', 
    'Title2', 
    'Title3', 
    'Title4', 
    'Title6',
    'Title7',
    'Title8',
    'Title9',
    'Pastafarianismin juhlat',
    'Suomalaiset nimipäivät',
    'Suomenruotsalaiset nimipäivät'
    ]  # Replace with your specific titles list

  for item in titleitems:
    title = item.get('title', '').decode('utf8')
    description = item.get('description', '').decode('utf8')
    
    # Remove everything before " - " in the title
    if " - " in title:
      title = title.split(" - ", 1)[1]

    # Add titles to specific list items
    for specific_title in specific_titles:
      if specific_title in title:
        filtered_items.append({'title': title, 'description': description})

  with open(filename, 'w') as jsonfile:
    json.dump(filtered_items, jsonfile, ensure_ascii=False, indent=4)
  logging.info(f"Data saved to {filename}")

def main():
  logging.info("Starting RSS feed processing")
  loadRSS()
  titleitems = parseXML('webcal-guru-today.xml')
  savetoJSON(titleitems, 'webcal-guru-today.json')
  logging.info("RSS feed processing completed")

if __name__ == "__main__":
  main()
