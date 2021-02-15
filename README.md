# Xdeck Startup Discovery
*Codename: 'Astral'*

### TechLabs Düsseldorf, Digital Shaper Program
### Winter Term 2020/2021, Project Group 14

**Developers**
* @franciscodlsb
* @pclp17

**Mentor support from**
* @semalfni


## Overview

**Astral** is an automated discovery tool tailored to the specific requirements of http://xdeck.de, an accelerator programme which supports early-stage, data-enabled, B2B tech startups with a focus on omnichannel solutions applicable in different industries. The project is supported by xdeck and https://www.techlabs.org/ Digital Shaper Program mentors and participants.


## Implemented Features
- Web Scraping:
   * in /First_Scripts/ "bakers_florida_indeed.ipynb" and "startbase.com_sample" are the initial scripts to learn webscrapping using first the indeeed.com website, and a single startup from startbase.com.
   * in /Deutsche_Startups/ "deu_startups.ipynb" and in /Startbase/ "starbase.com.ipynb" are the scripts to extract the links and information fo all the startups in each website. The templates can be used for finding further startups. "starbase.com.ipynb" includes the creation of a virtual browser with Selenium because to obtain the links of the startups from https://www.startbase.de/startups, some waiting time is needed.

- Data Merging:
   * "DataMerging.ipynb" merges and does an initial cleaning of the datasets obtained adding information from the most informative database to the least informative. Fields don't apepar in a datase are filled with nans
   * "dataframes_merge.ipynb" merges and does an initial cleaning of the datasets obtained using an exclusive criteria, obtaining only the mutual fields in both datasets.

- Data Filter:
   * "DataFilter.ipynb" performs an initial filtering as reequested by xdeck, obtaining the companies from NRW, with less than 3 years from funding, small team-size and B2B-B2C  focus.
   
- Data Visualization:
   * DataVis.ipynb: initial visualization of the scrapped data. Specifying the columns to visualize, it can be applied to filtered_startups or other extracted startups. For fields with multiple unique elements, it can plot the most frequent ones.


## Features to Implement
- Web Scraping: 
   * Modify new websites so that fields coincide before cleaning
   * Implement a bigger number of websites using the current templates as described in the xdeck pdf.
   * Add NLP for discovering new startups and fill out missing fields in current data

- Data Merging: 
   * Modify the cleaning process depending on the new added websites
   * Now it adds the missing fields when the same startups are added. But when a field is not empty, it shoudl be able to add information if there is a conflict, like members, if one database has more information than other, it should add up.
- Data Filter:
   * Stablish a filtering criteria when missing fields are present. Now they are included at the end of the fitlered startups
   * Implement a rating criteria with the matching percentage of xdeck or other companies needs. For this, a matching criteria must be used depending on how important is a specific category and how close is the field to the criteria. This has to be done after filtering startups that are left out.
- UI:
   * Create a user friendly interface/ web so that the filtering can be done at the request of the user


## Files
- Cities_NRW_DE and Cities_NRW_EN - list of cities in NRW for perfoming the data filtering in English and German.
- /Deutsche_Startups/deutsche_startups.csv - list of startups with info extracted from deutsche startups
- /Startbase/startbase.csv - list of startups with info extracted from startbase.com
- combined_startups.csv - combined startups maximizing information keeping all the columns
- list_startups.csv - combined startups with the minimum number of columns
- filtered_startups.xlsx - filtered startups from combined_startups.csv applying xdeck criteria
- 20201214_xdeck_techlabs_scouting_deep_dive - xdeck information on the scouting process


## Resources
- BeautifulSoup4 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Scrapy - https://docs.scrapy.org/en/latest/intro/overview.html
- Selenium - https://selenium-python.readthedocs.io/
- Web scrapping and using NLP - https://towardsdatascience.com/scraping-the-web-using-beautifulsoup-and-python-5df8e63d9de3


## Dataset
Obtained from:
https://www.startbase.com/
https://www.deutsche-startups.de/.

