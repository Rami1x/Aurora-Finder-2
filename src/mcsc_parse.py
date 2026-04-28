import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

column_name = ["name", "age", "gender", "last_seen", "from", "img_url"]


def get_prov(provinces:list) -> list:
    """
    returns the URL destination query for scraping.
    """

    url_queries = []

    prov_dict = {
        "AB": "Alberta",
        "BC": "BritishColumbia",
        "MB": "Manitoba",
        "NB": "NewBrunswick",
        "NL": "NewfoundlandandLabrador",
        "NS": "NovaScotia",
        "ON": "Ontario",
        "PE": "PrinceEdwardIsland",
        "QC": "Quebec",
        "SK": "Saskatchewan",
        "NU": "Nunavut",
        "NT": "NorthwestTerritories",
        "YT": "Yukon"
    }

    for prov in provinces:
        if prov not in prov_dict.keys():
            print(f"Province/Territory of {prov} is either not an official acronym or does NOT exist.")
            return None
        else:
            url_queries.append(prov_dict[prov])
    
    
    return url_queries


def get_all_prov() -> list:
    """
    Gets all the provinces url query
    """

    all_prov = ["AB","BC","MB","NB","NL","NS","ON","PE","QC","SK","NU","NT","YT"]
    return get_prov(all_prov)

def get_mcsc_link(prov:list) -> list:
    """
    Gets all the links for mcsc to start scraping
    """

    all_links = []

    for province in prov:
        all_links.append(f"https://www.mcsc.ca/missing-children-cases/?p={province}&o=missing&d=desc")
    
    return all_links


def get_parsed_data(url:str) -> list:
    """
    Gets text data and sorts into a list
    """
    parsed_data = []
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")


    cases = soup.find_all("div", class_="cell large-9 small-12")
    
    for case in cases:
        name = None
        age = None
        gender = None
        missing_since = None
        location = None

        text = case.get_text()

        for line in text.splitlines():
            line = line.strip()

            if ":" not in line:
                continue
        
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            match key:
                case "Name":
                    name = value
                
                case "Age":
                    age = value
                
                case "Gender":
                    if value == "boy":
                        gender = "Male"
                    elif value == "girl":
                        gender = "Female"
                    else:
                        gender = value

                case "Missing Since":
                    missing_since = value

                case "Location":
                    location = value

        parsed_data.append([
            name, 
            age, 
            gender, 
            missing_since, 
            location
            ])

            
    return parsed_data

def get_img_urls(url:str) -> str:
    """
    Gets img of missing child as a URL
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    img_urls = []
    
    img_divs = soup.find_all("div", class_="cell large-3 small-12")

    for div in img_divs:
        img = div.find("img")

        if not img:
            continue
        
        src = img.get("src") or img.get("data-src")

        if src:
            img_urls.append(src)

    return img_urls

