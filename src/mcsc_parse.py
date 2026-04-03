import pandas as pd

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

