# Programmed by Abdullah Suhail
# rating_chart.py
# 04/21/2018
# ITMD 413 Spring 2018 - Final Project
# Professor James Papademas
# This program will allow users to view and rate television shows
# from a database called shows.db using a GUI interface

# import the myDatabase file to use the functions defined in it
# import pygal to create charts
# import the os module so you can get us os functions
# import webbrowser to open a file in a web browser
# import numpy to perform math functions
from myDatabase import *
import pygal
import os
import webbrowser
import numpy as np


def displayRating():
    showrating = selectShowrating()
    # Insert each show name and rating into pygal chart
    bar_chart = pygal.Bar()  # create a bar graph object
    ratinglistavg = []
    for id, name, desc, rating in showrating:
        ratinglist = []
        ratinglist.append(rating)
        ratinglistavg.append(rating)
        bar_chart.add(name, ratinglist)  # Add some values
    average = (np.mean(ratinglistavg))
    bar_chart.add('Ratings Average', average)
    bar_chart.render_to_file('rating_chart.svg') # Save the svg to a file
    try:
        # open the file in a web browser
        filename = 'file:///'+os.getcwd()+'/' + 'rating_chart.svg'
        webbrowser.open_new_tab(filename)
    except OSError as e:
        print('Error with file: ' + e)





