import mcsc_parse as mcsc
import pandas as pd
import requests


data = {
    "Name" : [],
    "Age" : [],
    "Gender" : [],
    "Location" : [],
    "Missing Since" : [],
    "Image" : []
}

test = mcsc.get_all_prov()
mcsc_links = mcsc.get_mcsc_link(test)


for link in mcsc_links:
    cases = mcsc.get_parsed_data(link)
    case_images = mcsc.get_img_urls(link)
    i = 0

    for case in cases:
        name = case[0]
        age = case[1]
        gender = case[2]
        location = case[4]
        missing_since = case[3]

        data["Name"].append(name)
        data["Age"].append(age)
        data["Gender"].append(gender)
        data["Location"].append(location)
        data["Missing Since"].append(missing_since)
        
        if i < len(case_images):
            data["Image"].append(case_images[i])
        else:
            data["Image"].append(None)
        
        i += 1

case_dict = pd.DataFrame(data)
case_dict.to_csv("missing_people.csv", index=False)

print(case_dict)

