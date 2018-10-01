#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import pandas as pd

def histogram_times(filename):
    with open(filename) as f:
    	csv_reader = csv.reader(f)
    	data_list = list(csv_reader)
    time_column_number = 0
    output_list = np.zeros(24)
    for i in range(0, len(data_list)):
    	for j in range(0, len(data_list[i])):
    		if (data_list[i][j] == 'Time'):
    			time_column_number = j
    for i in range(1,len(data_list)):
    	if data_list[i][time_column_number]:
            time = ""
            count = 0
            for c in data_list[i][time_column_number]:
                if(not(c.isdigit()) and time != ""):
                    break
                elif(c.isdigit()):
                    time += c
            hours = int(time)
            if hours <= 23:
                output_list[hours] += 1
    return output_list

def weigh_pokemons(filename, weight):
    pokedex = pd.read_json(filename)
    pokedex = pd.read_json((pokedex['pokemon']).to_json(), orient = 'index')
    f = lambda x: float(x[0])
    pokedex.weight = pokedex.weight.str.split(" ").apply(f)
    names = pokedex[pokedex.weight == weight].name.tolist()
    return names

def single_type_candy_count(filename):
    pokedex = pd.read_json(filename)
    pokedex = pd.read_json((pokedex['pokemon']).to_json(), orient = 'index')
    f = lambda x: len(x)
    pokedex.type = pokedex.type.apply(f)
    return pokedex[pokedex.type == 1].candy_count.sum()

def reflections_and_projections(points):
    if (len(points) != 2):
        return None
    points[1] = 1 - (points[1] - 1)
    rotater = np.array([[0,-1],[1,0]])
    points = np.dot(rotater, points)
    projecter = np.array([[1,3],[3,9]])
    points = 0.1 * np.dot(projecter, points)
    return points

def normalize(image):
    if (np.shape(image) != (32,32)):
        return None
    image = image.astype(float)
    max_value = image.max()
    min_value = image.min()
    image = (image - min_value) * (255 / (max_value - min_value))
    return image


def sigmoid_normalize(image, a):
    if (np.shape(image) != (32,32)):
        return None
    image = image.astype(float)
    image = 255 * ((1 + np.exp(- ((a ** (-1)) * (image - 128)))) ** (-1))
    return image