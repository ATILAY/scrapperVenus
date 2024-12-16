import requests
from bs4  import BeautifulSoup
import pandas  as pd
from helper import elaborate_wage

canada_bc_occupations_list_url = "https://www.jobbank.gc.ca/wagereport/location/bc"

target_url = canada_bc_occupations_list_url

proceed = True

data = []

print('program starts..')

page = requests.get(target_url)

soup =  BeautifulSoup(page.text, "html.parser")

# print(soup) #first check point

all_occupations = soup.find_all("tr",class_="areaGroup")

for occupation in all_occupations:
    item = {}
    item['noc_code'] = occupation.find("span", class_="nocCode").text
    item['position'] = occupation.find("a").text.replace("\t","").replace("\n","")

    low_wage_str = occupation.find("td", {"headers": "header2a_wages"}).text.replace("\t","").replace("\n","").replace(" ","")
    median_wage_str = occupation.find("td", {"headers": "header2b_wages"}).text.replace("\t","").replace("\n","").replace(" ","")
    high_wage_str = occupation.find("td", {"headers": "header2c_wages"}).text.replace("\t","").replace("\n","").replace(" ","")

    item["low_wage"] = elaborate_wage(low_wage_str)
    item["median_wage"] = elaborate_wage(median_wage_str)
    item["high_wage"] = elaborate_wage(high_wage_str)

    item['position_detail_link'] = "https://www.jobbank.gc.ca" + occupation.find("a").attrs["href"]

    data.append(item)

# print(all_occupations) #second check point
# print(data) #third check point

df = pd.DataFrame(data)
df.to_csv("occupations.csv")
df.to_json("occupations.json",orient='records',lines=True)

print('please check .csv file..')
