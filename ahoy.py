# This driver script performs the following tasks
# (1) Move to the directory containing the automation scripts
# (2) Execute the automation scripts: auto.py and barca.py

import os

def main():
    os.chdir(r'C:\Users\HP\Documents\ATOM C++\Python 3 Bootcamp\ws_api_am\automation_scripts')
    os.system(r'python auto.py')
    os.system(r'python barca.py')

if __name__ == '__main__':
    main()
