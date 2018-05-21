# Programmed by Abdullah Suhail
# myDatabase.py
# 04/21/2018
# ITMD 413 Spring 2018 - Final Project
# Professor James Papademas
# This program will allow users to view and rate television shows
# from a database called shows.db using a GUI interface

# the sqlite3 module lets you create databases and manipulate them
# import show_data that has the data scraped from the "website" I created
import sqlite3
from sqlite3 import Error
import show_data

# function to create the database
def createDB():
    # create a database connection to a SQLite database
    try:
        conn = sqlite3.connect('shows.db')
    except Error as e:
        print('createDB Error: ', e)
    finally:
        print ('Database Created')
        conn.close()


# function to create the table in the database
def createTable():
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        c.execute('create table if not exists shows'
                  '(id integer primary key, show_name text not null, show_desc text not null, '
                  'show_rating integer)')
    except Error as e:
        print('createTable Error: ', e)
    finally:
        print('Table Created')
        c.close()
        conn.close()


# function to select a specific show description from the database
def selectShowdesc(show_name):
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        c.execute('select show_desc from shows where show_name = ?', (show_name,))
        show_desc = c.fetchone()
        return show_desc
    except Error as e:
        print ('selectShowdesc Error: ', e)
    finally:
        c.close()
        conn.close()


# function to select all the shows in the database
def selectShows():
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        c.execute('select show_name from shows')
        shows = c.fetchall()
        return shows
    except Error as e:
        print ('selectShows Error: ', e)
    finally:
        c.close()
        conn.close()


# function to select all the show ratings in the database
def selectShowrating():
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        c.execute('select * from shows where show_rating is not null')
        ratings = c.fetchall()
        return (ratings)
    except Error as e:
        print ('selectShows Error: ', e)
    finally:
        c.close()
        conn.close()


# function to populate database with the show names and descriptions from show_data
def insertShows():
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        for name, desc in show_data.show_name_desc:
            data = (name, desc)
            sql = 'insert into shows (show_name, show_desc) values (?,?)'
            c.execute(sql, data)
            conn.commit()
    except Error as e:
        print('insertShows Error: ', e)
    finally:
        print('Database Populated')
        c.close()
        conn.close()


# function to update a specific show rating in the DB
def updateShowrating(value, show_name):
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        sql = 'update shows set show_rating = ? where show_name = ?'
        data = (value, show_name)
        c.execute(sql, data)
        conn.commit()
    except Error as e:
        print ('updateShowrating Error: ', e)
    finally:
        print ('Rating for ' + show_name + ' has been Updated')
        c.close()
        conn.close()


# function to empty the shows table
def deleteShows():
    try:
        conn = sqlite3.connect('shows.db')
        c = conn.cursor()
        c.execute('delete from shows')
        conn.commit()
    except Error as e:
        print('deleteShows Error: ', e)
    finally:
        print('Table Emptied')
        c.close()
        conn.close()


# createDB()
# createTable()
# insertShows()
# selectShows()
# deleteShows()
