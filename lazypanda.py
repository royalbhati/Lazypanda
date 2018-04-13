import numpy as np
import pandas as pd



def usage():
	print(''' Currently supported functions

	checknull: checks if theres any null values in particular column of your dataset
				  >>    usage: 
				  		checknull('column_name') Note:Make sure your data is loaded as df
	
	sigmoid: returns sigmoid of any number or array specified
				  >>    usage:
				  		sigmoid('array or number')
				  		ex: >>sigmoid(0)
				  			>>0.5''')	  	


def checknull(f):
    return df[f].isna().value_counts()

def sigmoid(x):
	return 1/(1+np.exp(-x))




   

