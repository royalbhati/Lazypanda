import numpy as np
import pandas as pd



def usage():
	print(''' Currently supported functions

	checknull_column: checks if theres any null values in particular column of your dataset
				  >>    usage: 
				  		checknull('column_name') Note:Make sure your data is loaded as df
	
	checknull: checks if theres any null values in entire dataset
				  >>    usage: 
				  		checknull() Note:Make sure your data is loaded as df
	
	sigmoid: returns sigmoid of any number or array specified
				  >>    usage:
				  		sigmoid('array or number')
				  		ex: >>sigmoid(0)
				  			>>0.5''')	  	


def checknull_column(f):
    return df[f].isna().values.any(),('sum :',df[f].isna().values.sum())

ddef checknull():
    return df.isna().values.any(),('sum :',df.isna().values.sum())		

def sigmoid(x):
	return 1/(1+np.exp(-x))




   

