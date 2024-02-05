# UCL_Moodle_4_scraper
Python 3 program to scrape downloadable content off of UCL's virtual learning enviroment moodle. An updated version of the never-finished UCL moodle 3 scraper, adapted for the new moodle 4. Uses Selenium with Firefox. Pulls the downloadible content (PDFs, ZIPs, PPTs etc) into your default download folder.

Must have firefox installed to run.

# Usage

The main script is called scraper.py and can be called by entering the following command into your terminal: `python3 scraper.py [url_to scrape] [login email] [login password]`

```
usage: scraper.py url email password

positional arguments:
  - url              url of the of moodle page 
  - email            email used to login to moodle
  - password         password used to login to moodle
```
# Licence
Under MIT licence. Copies of this code can be freely modified, distributed, eaten for breakfast, etc. without restriction. 

# ToDo (This will never be done)
- DOCUMENTATION!
- General code cleaning/optimisation. 
- Add method to download mp4 files
- Add method to download non-directly embedded files
- Add Chrome support.
- Add method to preconfigure browser options
- Fix more bugs and blindspots yet to be found

