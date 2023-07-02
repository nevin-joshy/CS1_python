# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:14:36 2022

@author: Nevin Joshy

Given a time period and eighting for imdb rating and twitter ratings, this program
produces the best and worst movies within the time period using a imdb file containing all the movie
information, and a ratings file containg lists of twitter ratings 
"""

#imports json, allowing us to read json files
import json


"""main code"""
if __name__ == "__main__":
    
    """opens and reads json code"""
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    """input statements for min, max, w1, and w2. converts to ints and floats so
    the real values can be accessed later"""
    min_year = input("Min year => ").strip()
    print(min_year)
    min_year = int(min_year)
    max_year = input("Max year => ").strip()
    print(max_year)
    max_year = int(max_year)
    w1 = input("Weight for IMDB => ").strip()
    print(w1)
    w1 = float(w1)
    w2 = input("Weight for Twitter => ").strip()
    print(w2)
    w2 = float(w2)
    
    """This code adds all movies from the movies dictionary that are within the year bounds to a new
    dictionary called yearmovies"""
    yearmovies = dict()
    for movie in movies:
        if movies[movie]['movie_year']>=min_year and movies[movie]['movie_year']<=max_year:
            if (movie in ratings) and len(ratings[movie])>2:
                yearmovies[movie] = movies[movie]
    
    """while loop that executes code until brokes by stop command"""
    while True:
        #input statement for genre
        gen = input("\nWhat genre do you want to see? ").strip()
        print(gen)
        if gen.lower() == "stop":#checks if user is breaking code by checking for stop command
            break
        gen = gen.title()#converting gen to title so it can match contents of dictionary
        
        movielist = []#empty list to which movies in the genre will be added
        """code that checks the yearmovies dictionary for all movies that have the correct genre,
        and if they also have more than 2 ratings in the ratings dictionary, adds the rating based on the formula, the moviename, and the movieyear
        as a tuple to the movielist"""
        for movie in yearmovies:
            if gen in yearmovies[movie]['genre']:
                finalrating = (w1 * yearmovies[movie]['rating'] + w2 * (sum(ratings[movie]))/len(ratings[movie])) / (w1 + w2)
                movielist.append((finalrating, yearmovies[movie]['name'],yearmovies[movie]['movie_year']))
        #sorts movielist by rating in reverse order as newlist
        newlist = sorted(movielist, reverse=True)
        #if not movies in list, prints no movies found
        if len(newlist) ==0:
            print("\nNo {} movie found in {} through {}".format(gen,min_year,max_year))
            continue
        #formatting to print the best and worst movie with its year, name and rating
        print("\nBest:\n        Released in {}, {} has a rating of {:.2f}".format(newlist[0][2],newlist[0][1],newlist[0][0]))
        print("\nWorst:\n        Released in {}, {} has a rating of {:.2f}".format(newlist[-1][2],newlist[-1][1],newlist[-1][0]))
        