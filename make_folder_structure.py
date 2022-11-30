#!/usr/bin/env python3


import os
from shutil import copyfile

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

subfolder="dominik" #### CHANGE HERE!
template= "dominik_template.py" #### CHANGE HERE!

for day in range(1,26):
    folder_name = f'day_{str(day).zfill(2)}'
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f'{folder_name} already existed')

    subfoldername = f'{folder_name}{os.sep}{subfolder}'

    try:
        os.mkdir(subfoldername)
    except FileExistsError:
        print(f'{subfoldername} already existed')

    copyfile(template,f'{subfoldername}{os.sep}solution.py')

    with open(f'{subfoldername}{os.sep}input.txt', 'w') as f:
        f.write('I need input!')

