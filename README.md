# Ahoy

__Ahoy__ contains Python scripts which I have written while learning basic Web Scraping and Automation. These scripts help me complete daily tasks automatically which I used to do manually earlier, such as launching a few important applications and fetching the latest news of my favourite football club.

### [barca.py](barca.py)

* This script uses [*__requests__*](https://pypi.org/project/requests/) and [_**beautifulsoup4**_](https://pypi.org/project/beautifulsoup4/) modules for web scraping.
* It scrapes two renowned football websites, viz. [__Marca__](https://www.marca.com/en/) and [__Barca Blaugranes__](https://www.barcablaugranes.com/), for [__FC Barcelona__](https://www.fcbarcelona.com/en/) news.
* It then finds today's news articles (using [*__datetime__*](https://docs.python.org/3.8/library/datetime.html) module) and open them in new tabs in [__Google Chrome__](https://www.google.com/chrome/) (using [_**webbrowser**_](https://docs.python.org/3.8/library/webbrowser.html) module).

### [auto.py](auto.py)

* This script uses [*__os__*](https://docs.python.org/3.8/library/os.html) module to launch [__Google Chrome__](https://www.google.com/chrome/), [__Atom IDE__](https://atom.io/) and [__Jupyter Notebook__](https://jupyter.org/).
* You can change the script by adding paths to your preferred web browser and IDE.

### [ahoy.py](ahoy.py)

* This is a driver script which performs the following tasks (using the [*__os__*](https://docs.python.org/3.8/library/os.html) module):
* Move to the cloned directory containing the web scraping and automation scripts, viz. [__barca.py__](barca.py) and [__auto.py__](auto.py)
* Execute the aforementioned scripts

## Steps to use Ahoy

* Clone this repository to your local system.
* Add/Change the path variables for the web browser, IDE and Jupyter Notebook (if needed) in [__auto.py__](auto.py).
* Add/Change the path variable for the cloned repository (if needed) in[__ahoy.py__](ahoy.py).
* Add the path to the cloned repository as a *__Path__* __System Variable__ under the __Environment Variables__ section in __System Settings__.

#### NOTE:

* _Please make necessary and appropriate changes to file/directory paths in order to execute the scripts correctly._
* _You can take help from the instructions given in [README.md](README.md) and the comments present in the scripts._
* _All the file/directory paths and terminal/command prompt commands (to execute Python scripts) in each of the three scripts are written as Python raw strings._
