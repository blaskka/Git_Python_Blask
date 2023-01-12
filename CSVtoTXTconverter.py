# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:25:03 2023

@author: blask

Title: CSV to TXT codebook converter
"""

# Importing libraries

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file 

codebook_csv = pd.read_csv('C:/Users/blask/Documents/Zertifikatskurs/Modul2_IT & Data Science/2.5_Python/Assignment/Codebook_Test_revised.csv', encoding='cp1252', sep=';', on_bad_lines='skip')

print (codebook_csv)

# Create data frames for all columns in the CSV 

numb_var=pd.value_counts(codebook_csv['Position'], dropna=False)
numb_name=pd.value_counts(codebook_csv['Name'], dropna=False)
numb_label=pd.value_counts(codebook_csv['Label'], dropna=False)
numb_val=pd.value_counts(codebook_csv['Valid_values'], dropna=False)
numb_mis=pd.value_counts(codebook_csv['Missing_values'], dropna=False)

# Write size of the data frames for variable, name and label into distinct variables.

numb_var_s=numb_var.size
numb_name_s=numb_name.size
numb_label_s=numb_label.size

#Plot numb_var_s, numb_label_s, and numb_val_s in a bar chart

fig, ax=plt.subplots()

x_axis=['numb_var','numb_name','numb_label']
unique_values=[numb_var_s,numb_name_s,numb_label_s]
bar_colors=['tab:red', 'tab:orange', 'tab:blue']

ax.bar(x_axis, unique_values, color=bar_colors)
ax.set_ylabel('number unique values')
ax.bar_label(ax.containers[0], label_type='edge')
plt.show()

# Compare values of numb_var_s, numb_label_s, and numb_val_s

if numb_var_s!=numb_name_s or numb_var_s!=numb_label_s:
    print ("Please check your CSV file for duplets in the columns 'name' and 'label' and revise your file if necessary.")
else:
    print("CSV file ready for conversion.")
    
    new_text = open("Codebook_converted.txt", "w")
    
    # Convert information for one variable into a textblock in the file Codebook_converted.txt

    i = 0
    for Position, row in codebook_csv.iterrows():
            splitrow1 = row[1].split(" ") 
            for item1 in splitrow1: 
                new_text.write(item1 + "\n")
            splitrow2 = row[2].split ("\n") 
            for item2 in splitrow2: 
                new_text.write(item2 + "\n")
            splitrow3 = row[3].split("\n")
            for item3 in splitrow3: 
                new_text.write(item3 + "\n")
            splitrow4 = row[4].split("\n") 
            for item4 in splitrow4: 
                new_text.write(item4 + "\r\n")
    new_text.close()
    print("Completed: Finished converting variable information.")