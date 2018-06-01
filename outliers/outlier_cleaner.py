#!/usr/bin/python

import numpy as np

def getError(item):
    error = item[2]
    return error


""" Function: OutlierCleaner ---------------------------------------------------
    Goal:   To clean away 10% of the points with the largest residual error
            (difference between the prediction & actual net worth). We give it
            all of the data points we have & it gives us 90% of the data points
            with the smallest error.
            
    Input:  1. predictions: All of the predictions
            2. ages: All the 'x' value in our input data like ages
            3. net_worths: All the 'y' value in our input like net_worth
            
    Output: Returns a tuple named 'cleaned_data'. Each tuple is of the form
            (age, net_worth, error)
-----------------------------------------------------------------------------"""
def outlierCleaner(predictions, ages, net_worths):
    cleaned_data = []

    ### Obtains Tuple of Age, Net_worth, Error
    for idx, item in enumerate(net_worths):
        # Calculates Error        
        error = predictions[idx] - item
        
        # Creates Tuple
        row = (int(ages[idx]), float(net_worths[idx]), np.abs(float(error)))
        cleaned_data.append(row)
    
    # Sorts & keeps best 90% of set
    cleaned_data = sorted(cleaned_data, key=getError)
    cleaned_data = cleaned_data[:int(round(len(cleaned_data)*.9))]
    #print cleaned_data
    
    return cleaned_data
