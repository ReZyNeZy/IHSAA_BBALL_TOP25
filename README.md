# IHSAA Top 25 Basketball Webscraper

## Overview

 This application is a webscraper designed to access the popular prep sports reporting/stat site Maxpreps. More specifically, this program access the leaderboard for all 4 divisions of Indiana basketball and convert the tables on screen into a python list of all. The program also takes the "Overall" section, which displays the leaders of all 4 divisions combined, and addes this table to the list too. 

This program utelizes Project Jupyter's JupyterLab as the coding environment. JupyterLab was used as this is a project based on data harvesting and manipulation which is the main selling point of JupyterLab. JupyterLab also allows for sepration of coding cells which makes the program easier to digest be allowing for similar tasks to be run together and reduction of a need to rerun lines of code for every run of the program. The information given by the tables on Maxpreps updates daily to weekly and not queurying them for every run of the program respects the integrety of the website. JupyterLab also utelizes python3 as the primary coding language. Python3 has many tools and extensions that allow for easy retreaval of HTML on webpages through imports such as requests. This data is able to be manipulated via the pandas extension. Pandas allows for easy manipulation of HTML and data.

This program was desinged to dip my feet into the world of APIs, webscraping, and further explore data science. As such. this program is quite short and seemingly "useless". If I am to update this program. I hope to use the skills I have learned in creating this project to gather data of the top student-athletes in the state of Indiana. This data would then be fed to a machine learning algorithm to predict the winner of the "Mr. Basketball" award for the year. If I were to continue working on this project, I would expand the rankings to that of different sports, or to multiple states. 

##Installation and Runtime

This program was made using JupyterLab and is sectioned off into coding cells. In order to maintain this level of separation, it is recommended that this program is edited, and ran in the JuptyterLab or Jupyter Notebook environment. A download of Anaconda is a great tool to use to gain access to JupyterLab and Jupyter Notebook. Project Jupyter also supports a browser version of their 

When running this program, it is important to respect the origional authors of the data and the website in which the table came from. To respect Maxpreps, PLEASE DO NOT RUN THE WEB SCRAPING FUNCTION OF THIS CODE MORE THAN ONCE PER DAY. Maxpreps only updates their rankings once per day or even once per week as previously stated. It is frivilous to run this portion of the program unless the rankings have been changed. Running this portion would only seek to query Maxpreps more times than needed and is disrespectful.

