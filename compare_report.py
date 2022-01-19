"""
@ Author: Michael Calafato
"""
# LIBRARIES
import pandas as pd

"""
FUNCTIONS
"""

def read_file(file):
    """Load data from file."""
    with open(file) as f_read:
        # store as list
        my_content = f_read.readlines()

        # remove new line
        content = [n.replace("\n","") for n in my_content]
            
        # remove header
        content.pop(0)
    return content

def create_dict(content):
    """Build dictionary to store transactions by user."""
    dict = {}
    for i in content:
        keys = dict.keys()
        # breakdown elements in row
        row = i.split(',')
        # fetch id
        id = row.pop(0)
        # store in dictionary
        if id in keys:
            dict[id] += row[2]
        else:
            dict[id] = row
    return dict

def compare_records(dict_1, dict_2):
    """Returns transactions that do not match in both dicts. """
    dict_2_keys = dict_2.keys()
    
    # loop through transactions by patient id
    for x in dict_1:
        # check patient ids entered in state site, check the amount entered.
        if x in dict_2_keys and dict_1[x][2:] == dict_2[x][2:]:
            pass
        # output message if patient id not entered in state site.
        elif x not in dict_2_keys:
            print('ID: ', x, '\nLocal: ', dict_1[x],'\nNJMMP: NOT ENTERED \n')
        else:
            # output msg if patient amount does not match
            print('ID: ', x, '\nLocal: ', dict_1[x],'\nNJMMP: ', dict_2[x],'\n')
            

# TEST FILES
f_local = 'local_file.csv'
f_njmmp = 'njmmp_file.csv'

# RECORDS
local_dict = create_dict(read_file(f_local))
njmmp_dict = create_dict(read_file(f_njmmp))

# TRANSACTIONS
local_value = local_dict.values()
njmmp_value = njmmp_dict.values()

# PATIENTS
local_key = local_dict.keys()
njmmp_key = njmmp_dict.keys()

# RUN REPORT
compare_records(local_dict, njmmp_dict)