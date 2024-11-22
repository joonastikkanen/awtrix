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
  with open('webcal-guru-flagday.xml', 'wb') as f:
    f.write(resp.content)
  logging.info("RSS feed saved to webcal-guru-flagday.xml")

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
  filtered_items = []
  flag_icon = "🇫🇮"

  logging.info(f"Filtering title items from JSON file {filename}")
  for item in titleitems:
    if 'title' not in item:
      continue
    title = item.get('title', '').decode('utf8')
    description = item.get('description', '').decode('utf8')
    
    # Only process items with the Finnish flag icon
    if flag_icon in title:
      # Remove everything before the flag icon in the title
      title = title.split(flag_icon, 1)[1].strip()
      
      if "Tämän kalenterin tarjoaa" in description:
        description = description.split("Tämän kalenterin tarjoaa", 1)[0]

      filtered_items.append({'flagday': title, 'description': description})
    else:
      filtered_items.append({'flagday': "No flagday", 'description': "N/A"})
  
  logging.info(f"Saving {len(filtered_items)} items to JSON file {filename}")

  with open(filename, 'w') as jsonfile:
    json.dump(filtered_items, jsonfile, ensure_ascii=False, indent=4)
  logging.info(f"Data saved to {filename}")

def main():
  logging.info("Starting RSS feed processing")
  loadRSS()
  titleitems = parseXML('webcal-guru-flagday.xml')
  savetoJSON(titleitems, 'webcal-guru-flagday.json')
  logging.info("RSS feed processing completed")

if __name__ == "__main__":
  main()
