# riotapi-mysql

## Description

This project provides 4 files: 

  - [api_info](api_info.md) Steps to get a successfull api call

  - [mysql tutorial](mysql_tutorial.md) Tutorial on how to connect to mysql server, create database, table and collumns

  - [riot_api_data](riotapi_mysql/riot_api_data.py) Python script to fetch data from the Riot Games Developer API, formats data and stores them into final_list
  
  - [data_to_sql](riotapi_mysql/data_to_sql.py) Python script that inserts data to mysql database


## My Workflow Process
- First i focused on fetching data from riot dev api [Riot Developer](https://developer.riotgames.com). I created requests for all the data I needed and lastly created statements to check specific conditions or to ad data based on specific parameters

- Second step was setting up mysql server and accessing server on mysql workbench. If you have windows as operatng system and want to see a step by step proccess of setting up your mysql server and mysql workbench watch this tutorial
  [How to Install MySQL on Windows by Database Star](https://youtu.be/2om3byn2lxs?si=S6or78IJIlKCKr7i)

- Third step was creating a mysql database, table and colunms for api data [mysql.md](mysql_tutorial.md)

- Fourth step was inserting data into mysql database


## Contributing

Contributions to this project are welcome. You can help improve data fetching, add additional features, or enhance database interaction.


**NOTE**

This is my first bigger project so i believe many things in my code could be better optimised or work more efficiently.


Thank you for reading
