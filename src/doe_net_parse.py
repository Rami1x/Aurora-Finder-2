from bs4 import BeautifulSoup
import requests

def get_male_links() -> list:
    """
    Gets all the links for each cases
    """

    links = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    url = "https://www.doenetwork.org/mp-geo-canada-males.php"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    cases = soup.find_all("ul", class_="rig")
    for case in cases:
        a_links = case.find_all("a")

        for link in a_links:
            if link:
                href = link.get("href")
                if href.startswith("http"):
                    links.append(href)

    return links

def clean_links(links:list) -> list:
    """
    Fix link and change it to the updated fully requested link
    """
    fixed_links = []

    for link in links:
        identity = link[-13:]
        format = f"/software/mp-main.html?id={identity}"
        new_link = "https://www.doenetwork.org/cases" + format
        new_link = new_link[0:-5]
        fixed_links.append(new_link)
    
    return fixed_links

def get_parsed_data(link:str) -> list:
    """
    Gets data in list form
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    span = soup.find("span", id="form-part-1")

    print(soup)

lnk = get_male_links()
print(lnk[1])
print(lnk[2])
print(lnk[3])
print(lnk[4])
print(lnk[5])
fix = clean_links(lnk)
print(fix[7])
#get_parsed_data(lnk[2])