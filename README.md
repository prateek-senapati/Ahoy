# Ahoy

__Ahoy__ contains Python scripts which I have written while learning basic Web Scraping and Automation.

### [barca.py](barca.py)

* This script uses [*__requests__*](https://pypi.org/project/requests/) and [_**beautifulsoup4**_](https://pypi.org/project/beautifulsoup4/) modules for web scraping. 
* It scrapes two renowned football websites, viz. [__Marca__](https://www.marca.com/en/) and [__Barca Blaugranes__](https://www.barcablaugranes.com/), for [__FC Barcelona__](https://www.fcbarcelona.com/en/) news. 
* It then finds today's news articles (using [*__datetime__*](https://docs.python.org/3.8/library/datetime.html) module) and open them in new tabs in [__Google Chrome__](https://www.google.com/chrome/) (using [_**webbrowser**_](https://docs.python.org/3.8/library/webbrowser.html) module).

### [auto.py](auto.py)

* This script uses [*__os__*](https://docs.python.org/3.8/library/os.html) module to launch [__Google Chrome__](https://www.google.com/chrome/), [__Atom IDE__](https://atom.io/) and [__Jupyter Notebook__](https://jupyter.org/).

### [ahoy.py](ahoy.py)

* This is a driver script which performs the following tasks (using the [*__os__*](https://docs.python.org/3.8/library/os.html) module):
  * Move to the directory containing the web scraping and automation scripts, viz. [__barca.py__](barca.py) and [__auto.py__](auto.py)
  * Execute the aforementioned scripts
