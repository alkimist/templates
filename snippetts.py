import requests
import os
import re
from bs4 import BeautifulSoup as bs
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

path_string = "/home/kim/.working_data/AHH/"
Base = declarative_base()
engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

############################################################
## script to scrape wikipedia page of all current
## circulating currencies and currency symbols in the world
##
##########################################################

# Base.metadata.create_all(engine)

# resp = requests.get(
#     "https://en.wikipedia.org/wiki/List_of_circulating_currencies")
# soup = bs(resp.text)
# currency_table = soup.find(
#     name='table', attrs={'class': ['wikitable', 'sortable']})
# currency_table = currency_table.find('tbody')

# res = set()

# for row in currency_table.find_all('tr'):
#     curr_data_tags = row.find_all('td')

#     if len(curr_data_tags) > 3:
#         name = curr_data_tags[1].a.string.strip(
#         ) if curr_data_tags[1].a else None
#         symbol = curr_data_tags[2].string.strip(
#         ) if curr_data_tags[2].string else None
#         iso = curr_data_tags[3].string.strip(
#         ) if curr_data_tags[3].string else None
#         curr_data = name, iso, symbol
#         res.add(curr_data)


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def find_prf_files(startparth):
    res = []
    prf_pattern = re.compile(r'.+payment(\W|_)+request.*', re.IGNORECASE)

    for root, dirs, files in os.walk(startparth):
        for f in files:
            if prf_pattern.search(f):
                res.append(f)
    return sorted(res, reverse=True)
