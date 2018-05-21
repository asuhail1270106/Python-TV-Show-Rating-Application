# Programmed by Abdullah Suhail
# show_data.py
# 04/21/2018
# ITMD 413 Spring 2018 - Final Project
# Professor James Papademas
# This program will allow users to view and rate television shows
# from a database called shows.db using a GUI interface

# the requests module lets you take source code from http pages (html)
# beautiful soup lets you parse html code
import requests
from bs4 import BeautifulSoup

# I created a repo with bare bones data needed for my tv rating app
# the following lines fetch the html code from the specified link
r = requests.get("https://asuhail1270106.github.io/ITMD-413_FP/")
response = BeautifulSoup(r.text, 'html.parser')

'''
rlist = response.find_all('li')
for result in rlist:
    results = result.text
    items = results.split('\n')
    shows = list(items)
    print(shows)
'''

# the following code takes the requests response and parses it to create lists with information on shows
rlist = response.find_all('ul', attrs={'id': 'shows'})
show_name = []
for result in rlist:
    shows = result.find_all('li')  # finds html code encased in <li> tags
    for results in shows:
        show_name.append(results.text)
# print(show_name)

rlist = response.find_all('ul', attrs={'id':'shows_desc'})
show_desc = []
for result in rlist:
    shows = result.find_all('li')
    for results in shows:
        show_desc.append(results.text)
# print(show_desc)

# the previous lists that were created are sewn together element wise
show_name_desc = [list(a) for a in zip(show_name, show_desc)]
# print(show_name_desc)

