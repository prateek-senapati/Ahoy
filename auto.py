# Script to launch Google Chrome, Atom IDE and Jupyter Notebook

import os

def main():
    # browser_path contains the path to the web browser (here, Google Chrome) executable file
    browser_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    # ide_path contains the path to the IDE (here, Atom IDE) executable file
    ide_path = r'C:\Users\HP\AppData\Local\atom\atom.exe'

    # jupyter_nb_path contains the path to the Jupyter Notebook shortcut/link to the original executable file
    jupyter_nb_path = r'C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Jupyter Notebook (Anaconda3).lnk'

    # The aforementioned path variables can also contain paths to shortcuts/links to the respective executable files

    os.startfile(browser_path)
    os.startfile(ide_path)
    os.startfile(jupyter_nb_path)

if __name__ == '__main__':
    main()
