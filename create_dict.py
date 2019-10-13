import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import yaml
import re

def fix_format(word):
    word = word.replace(" ", "_")
    word = word.replace(".", "")
    word = word.lower()
    return word

def create_dictionary():
    url = 'http://www.orangecountync.gov/151/Accepted-Materials-List'
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    #headers = webpage.findAll('h2')
    #print(headers)
    #dni = webpage.findAll('')

    recycle_dict = {}

    trial = soup.findAll('tr')
    for section in trial:
        if (section.li != None):
            key = str(section.td.h2.contents[0])
            #print(key)
            recycle_dict[key] = {}
            values = re.split(', | or | & ', key)
            #print(value)
            recycle_dict[key]['Include'] = []
            for x in values:
                x = fix_format(x)
                recycle_dict[key]['Include'].append(x)
            #print(recycle_dict[key]['Include'], key)
            recycle_dict[key]['Do not include'] = []
            for td in section:
                if (td.strong != None):
                    try:
                        for item in td.ul:
                            value = item.contents
                            value = str(value[0])
                            value = value.replace("\xa0", "")
                            values = re.split(', | or | & | and ', value)
                            for x in values:
                                x = fix_format(x)
                                recycle_dict[key]['Do not include'].append(x)
                            #recycle_dict[key]['Do not include'].append(value)
                    except:
                        continue
    #print(recycle_dict)

    d = recycle_dict
    with open('result.yaml', 'w') as yaml_file:
        yaml.dump(d, yaml_file, default_flow_style=False)
