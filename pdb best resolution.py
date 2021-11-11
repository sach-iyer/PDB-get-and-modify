# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:59:57 2021

@author: sachi
"""

##      script for accessing the APIs of RCSB and choosing best resolution

##                  Importing packages
import requests
import numpy as np
import pandas as pd

##                      Read TSV of UniProt, and modify df

required_proteins_tsv_path = r""
best_pdb_csv_path = r""

df_proteins = pd.read_csv(required_proteins_tsv_path, sep = '\t', index_col = 'Entry')

df_proteins.insert(len(df_proteins.columns),'Best PDB',np.nan)
df_proteins.insert(len(df_proteins.columns),'Resolution',np.nan)

##                      Function defenition

def find_best_pdb(list_all_pdb, search_result):
    
    best_pdb = list_all_pdb[0]
    
    try:
        min_resln = search_result['data']['entries'][0]["rcsb_entry_info"][        "resolution_combined"][0]
    
    except TypeError:
            print("TypeError: * i = 0 *")
            min_resln = np.inf
            best_pdb = "ERRO"
            
    
    
    for i in range(len(list_all_pdb)):
        
        
        try:
            resln = search_result['data']['entries'][i]["rcsb_entry_info"][        "resolution_combined"][0]
        
        except TypeError:
            print("TypeError: i, min_resln, best_pdb = ",i,min_resln,best_pdb)
            
        
        else:
            if resln < min_resln:
                min_resln = resln
                best_pdb = list_all_pdb[i]
            
    return best_pdb, min_resln



for entry in df_proteins.index:
    
    print("Entry: ", entry)
    
    all_pdb_temp = df_proteins.loc[entry,'PDB']
    all_pdb = '"'
    
    if (type(all_pdb_temp) == str):
        
        list_all_pdb = all_pdb_temp.split(';')
        list_all_pdb.pop()
        
        for i in range(len(all_pdb_temp)-1):
            
            char = ''
            
            if all_pdb_temp[i] == ';':              #Convert string to right format, then change the search API
                all_pdb += '","'
                
            else:    
                all_pdb += all_pdb_temp[i]
                
        all_pdb += '"'
        
                
        #print('searching')                  #testing
                        
        search_result = requests.get(r'https://data.rcsb.org/graphql?query={entries(entry_ids:[' + all_pdb + r']){rcsb_entry_info {resolution_combined}}}').json()
        
        #print('JSON receieved')
        
        best_pdb, min_resln = find_best_pdb(list_all_pdb, search_result)
    
        
        df_proteins.loc[entry,'Best PDB'] = best_pdb
        df_proteins.loc[entry,'Resolution'] = min_resln
        
        print(entry, " : ", best_pdb, min_resln)
        
print("To CSV")

df_proteins.to_csv(best_pdb_csv_path)

print("Done")