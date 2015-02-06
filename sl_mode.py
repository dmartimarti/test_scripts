#!/usr/bin/python3

import pandas as pd 
import xlrd
from pandas import ExcelWriter

# py_slidingWindow_xlsx release information
__version__ = '0.0.1'
_verdata = 'Feb 2015'
_devflag = True


#########################################################################> MAIN

# Program Header
print('\n=-= py_slidingWindow_xlsx =-= v' + __version__ + ' =-= ' +
      _verdata + ' =-= by DLS team =-=')
if(_devflag): 
    print('\n>>> WARNING! THIS IS JUST A DEVELOPMENT SUBRELEASE.' + 
          ' USE IT AT YOUR OWN RISK!')  

file_name = "MPHM.xlsx"

xl_file = pd.ExcelFile(file_name)

dfs = {sheet_name: xl_file.parse(sheet_name)
	for sheet_name in xl_file.sheet_names}

# slow slmode version (as R script)

def slmode(size, output):
	writer = ExcelWriter(output)
	columnas = dfs["h_male_feces"].columns # store columns names
	length = len(dfs["h_male_feces"].columns)
	new_df = pd.DataFrame(dfs["h_male_feces"].iloc[:,0])
	for i in range(1,length-(size-1)):
		for j in range(0,(size)):
			new_df[str(columnas[j+i])] = dfs["h_male_feces"].iloc[:,j+i]
		new_df.to_excel(writer,"set " + str(i), index=False)
		new_df = pd.DataFrame(dfs["h_male_feces"].iloc[:,0])
	writer.save()


slmode(4, "male_feces_test.xlsx")



###############
##  TO DO:
##		- see if I can extract the name of each column. That should be in the reading_sheet loop above, I have to see
##		  which options I have to modify
##  	- create a loop to iterate over each column. Slow slmode as the R script
## 		-





