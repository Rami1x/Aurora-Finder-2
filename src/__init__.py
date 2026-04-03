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

df = pd.DataFrame(data)
df.loc[len(df)] = ["Test", 24, "Male", "Calgary", "2026-04-03", "image.jpg"]


for link in mcsc_links:
    current_html = requests.get(link)
    print(current_html)
