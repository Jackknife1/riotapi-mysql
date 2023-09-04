# api_info

**Description**

In this file i'll tell you steps how to fetch data from riot api

# Workflow process

  **1. We need to get API Key from [riot_developer](https://developer.riotgames.com)**
   
  **2. We need to get API URL for specific data (summoner-v4: gives you data about summoner like level, puuid, summoner name etc.)**
  
  **3. We need to puzzle together full API link**

    last_match_url = last_match_url + '&api_key=' + api_key
    
  **4. We call a request and save response in json data file**
  
    last_match_id = resp2.json()

  **5. We need to call key names from json file and we then get values assigned under that key name**

    puuid = player_info['puuid'] 

  **6. We can store all sorts of data into variables, then create a tuple containing those variables with data, wich can be inserted into database**
  
    final_list = (summoner_name, level, kills, asissts, deaths, kda)

  **NOTE**
  
  In [riot_api](riot_api.py) are 27 data variables that i found usefull for me
  
  You can store even more data in database or find new ways to obtain another usefull data about player or match

  Thank you for reading
