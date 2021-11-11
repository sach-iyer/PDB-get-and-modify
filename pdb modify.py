# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:34:59 2021

@author: sachi
"""

# Modifying pdb files [WORK IN PROGRESS]

ori_file_path = r""
modi_file_path = r""
req_chain = ''

ori_file = open(ori_file_path,"r").read()

modi_file = open(modi_file_path,"r").read()

all_lines = ori_file.split('\n')

new_lines = []

#Removing all except ATOM lines of chain

for i in range(len(all_lines)):
    
    line = all_lines[i]
    
    if line[0:4] == 'ATOM':
        if line[21] == req_chain:
            new_lines.append(line)
        
    elif line[0:3] == "END":
        new_lines.append(line)
        break