# api_info

**Description**

In this file i'll tell you steps how to fetch data from riot api

## Workflow process

1. First we need to get API Key from [riot_developer](https://developer.riotgames.com)
   
2. Then we need to get API URL for specific information (summoner-v4: gives you information about summoner like level, puuid, summoner name etc.)
  
3. Then we need to puzzle together full API link
   <p>
   <part>
   `last_match_url = last_match_url + '&api_key=' + api_key`
   </part>
   </p>
