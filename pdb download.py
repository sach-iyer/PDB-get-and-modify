# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:02:10 2021

@author: sachi
"""

# For downloading relevant pdb files

import requests

set_of_id = {}
download_location = r""

for pdb_id in set_of_id:
    
    response = requests.get("https://files.rcsb.org/download/"+ pdb_id +".pdb")
    
    print("response", pdb_id)
    
    open(download_location + "\\" + pdb_id + ".pdb","wb").write(response.content)
    
    print(pdb_id, "saved. \n")