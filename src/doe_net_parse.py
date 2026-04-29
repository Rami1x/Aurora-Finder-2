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
        start = link.find("cases/")
        end = start + 6
        link_format = link[end:]
        feilds = "&fields=true"
        url_scheme = f"/software/php/mpdatabase.php?id={link_format}"
        new_link = f"https://www.doenetwork.org/cases{url_scheme}"
        new_link = new_link[0:-5] + feilds
        fixed_links.append(new_link)
    
    return fixed_links


def get_parsed_data(link:str) -> list:
    """
    Gets data in list form
    """
    name = None
    age = None
    gender = None
    missing_since = None
    location = None
    list_output = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    r = requests.get(link, headers=headers)

    
    soup = BeautifulSoup(r.text, "html.parser")
    soup = str(soup.find("span").get_text(strip=True))
    pname = len('"pname"')


    # Name parse
    name_index_start = soup.find('"pname')
    name_index_end = name_index_start + pname + 1
    counter = 0
    name = ""
    for text in soup[name_index_end:]:
        if text == '"':
            if counter >= 2:
                break
            else:
                counter += 1
        else:
            name += text
    
    if name[-1] == ",":
        name = name.strip(",")
    
    # Age Parse
    age_text = len('"age":') + 1
    age_index = soup.find('"age":')
    age_index_end = age_index + age_text

    age = ""
    for text in soup[age_index_end:]:
        if text.isalpha():
            break
        else:
            age += text

    # Gender Parse
    gender_index = len('"gender":')
    gender_index_start = soup.find('"gender":')
    gender_index_end = gender_index + gender_index_start

    gender = ""
    counter = 0

    for text in soup[gender_index_end:]:
        if text == '"':
            if counter >= 2:
                break
            else:
                counter += 1
        else:
            gender += text

    
    gender = gender.strip(",")
        
    # Missing Since
    missing_since_text = len('"missing_since":')
    missing_since_index = soup.find('"missing_since"')
    missing_since_index_end = missing_since_text + missing_since_index

    missing_since = ""
    counter = 0

    for text in soup[missing_since_index_end:]:
        if text == '"':
            if counter >= 2:
                break
            else:
                counter += 1
        else:
            missing_since += text
    
    missing_since = missing_since.strip(",").replace(",", "")

    # Location Parse
    location_text = len('"location_last_seen":')
    location_index = soup.find('"location_last_seen":')
    location_index_end = location_index + location_text

    location = ""
    counter = 0

    for text in soup[location_index_end:]:
        if text == '"':
            if counter >= 2:
                break
            else:
                counter += 1
        else:
            location += text
    
    location = location.strip(",").replace(",", "")
    
    print(name, age, gender, missing_since, location)

lnk = get_male_links()
print(lnk[1])
print(lnk[2])
print(lnk[3])
print(lnk[4])
print(lnk[5])
fix = clean_links(lnk)
print(len(fix[2]))
get_parsed_data(fix[13])