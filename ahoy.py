# This driver script performs the following tasks
# (1) Move to the cloned directory containing the web scraping and automation scripts, viz. barca.py and auto.py
# (2) Execute the aforementioned scripts

import os

def main():
    clone_path = r'C:\Users\HP\Ahoy' # clone_path contains the path to the cloned repository
    os.chdir(clone_path)
    os.system(r'python auto.py')
    os.system(r'python barca.py')

if __name__ == '__main__':
    main()
