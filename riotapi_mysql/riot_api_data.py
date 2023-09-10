#Imports module requests for reguesting api calls 
import requests


#Summoner name and region 
name = "your_summoner_name"  #input("What is your summoner name:? ")
region = "your_region"  #input("What is your region?(eun1, euw1, na1, la1, la2, oc1, jp1): ")


#Formating region
formated_region = ""

if region == "eun1" or "euw1":
    formated_region = "europe"
elif region == "na1" or "la1" or "la2":
    formated_region = "america"
elif region == "br1":
    formated_region = "brazil"
elif region == "oc1":
    formated_region == "oceania"
elif region == "tr1":
    formated_region = "turkey"
elif region == "jp1":
    formated_region = "japan"
else:
    print("Invalid region")


#API key and formated API URL
api_key = ""
api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
api_url = api_url + '?api_key=' + api_key


#Data about player in json
resp1 = requests.get(api_url)
player_info = resp1.json()


#Player puuid and name
puuid = player_info['puuid']
summoner_name = player_info['name']


#Formated API URL for last played game
last_match_url = f'https://{formated_region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1'
last_match_url = last_match_url + '&api_key=' + api_key


#Getting response and selection last match id by index 
resp2 = requests.get(last_match_url)
last_match_id = resp2.json()
last_game = last_match_id[0]

#Formated API URL for last match data
match_id_url = f'https://{formated_region}.api.riotgames.com/lol/match/v5/matches/{last_game}'
match_id_url = match_id_url + '?api_key=' + api_key


#Last match data in json
resp3 = requests.get(match_id_url)
last_match_data = resp3.json()


#Index of player
part_index = last_match_data['metadata']['participants'].index(puuid)


#Data from last match
matchid = last_match_data['metadata']['matchId']
queueid = last_match_data['info']['queueId']
gameduration = last_match_data['info']['gameDuration']
queueid = last_match_data['info']["queueId"]


#Players team id
my_teamid = last_match_data['info']['participants'][part_index]['teamId']


#Puuids of all players
part1 = last_match_data['info']['participants'][0]['puuid']
part2 = last_match_data['info']['participants'][1]['puuid']
part3 = last_match_data['info']['participants'][2]['puuid']
part4 = last_match_data['info']['participants'][3]['puuid']
part5 = last_match_data['info']['participants'][4]['puuid']
part6 = last_match_data['info']['participants'][5]['puuid']
part7 = last_match_data['info']['participants'][6]['puuid']
part8 = last_match_data['info']['participants'][7]['puuid']
part9 = last_match_data['info']['participants'][8]['puuid']
part10 = last_match_data['info']['participants'][9]['puuid']


#Indexing all participants by puuid
part1_index = last_match_data['metadata']['participants'].index(part1)
part2_index = last_match_data['metadata']['participants'].index(part2)
part3_index = last_match_data['metadata']['participants'].index(part3)
part4_index = last_match_data['metadata']['participants'].index(part4)
part5_index = last_match_data['metadata']['participants'].index(part5)
part6_index = last_match_data['metadata']['participants'].index(part6)
part7_index = last_match_data['metadata']['participants'].index(part7)
part8_index = last_match_data['metadata']['participants'].index(part8)
part9_index = last_match_data['metadata']['participants'].index(part9)
part10_index = last_match_data['metadata']['participants'].index(part10)


#Teamid of all participants
idparticipant1 = last_match_data['info']['participants'][part1_index]['teamId']
idparticipant2 = last_match_data['info']['participants'][part2_index]['teamId']
idparticipant3 = last_match_data['info']['participants'][part3_index]['teamId']
idparticipant4 = last_match_data['info']['participants'][part4_index]['teamId']
idparticipant5 = last_match_data['info']['participants'][part5_index]['teamId']
idparticipant6 = last_match_data['info']['participants'][part6_index]['teamId']
idparticipant7 = last_match_data['info']['participants'][part7_index]['teamId']
idparticipant8 = last_match_data['info']['participants'][part8_index]['teamId']
idparticipant9 = last_match_data['info']['participants'][part9_index]['teamId']
idparticipant10 = last_match_data['info']['participants'][part10_index]['teamId']


#All articipants asissts
part1_a = last_match_data['info']['participants'][part1_index]['assists']
part2_a = last_match_data['info']['participants'][part2_index]['assists']
part3_a= last_match_data['info']['participants'][part3_index]['assists']
part4_a = last_match_data['info']['participants'][part4_index]['assists']
part5_a= last_match_data['info']['participants'][part5_index]['assists']
part6_a = last_match_data['info']['participants'][part6_index]['assists']
part7_a = last_match_data['info']['participants'][part7_index]['assists']
part8_a = last_match_data['info']['participants'][part8_index]['assists']
part9_a = last_match_data['info']['participants'][part9_index]['assists']
part10_a = last_match_data['info']['participants'][part10_index]['assists']


#All participants kills
part1_k= last_match_data['info']['participants'][part1_index]['kills']
part2_k = last_match_data['info']['participants'][part2_index]['kills']
part3_k = last_match_data['info']['participants'][part3_index]['kills']
part4_k = last_match_data['info']['participants'][part4_index]['kills']
part5_k = last_match_data['info']['participants'][part5_index]['kills']
part6_k = last_match_data['info']['participants'][part6_index]['kills']
part7_k = last_match_data['info']['participants'][part7_index]['kills']
part8_k = last_match_data['info']['participants'][part8_index]['kills']
part9_k = last_match_data['info']['participants'][part9_index]['kills']
part10_k = last_match_data['info']['participants'][part10_index]['kills']


#All participnats deaths
part1_d = last_match_data['info']['participants'][part1_index]['deaths']
part2_d = last_match_data['info']['participants'][part2_index]['deaths']
part3_d = last_match_data['info']['participants'][part3_index]['deaths']
part4_d = last_match_data['info']['participants'][part4_index]['deaths']
part5_d = last_match_data['info']['participants'][part5_index]['deaths']
part6_d = last_match_data['info']['participants'][part6_index]['deaths']
part7_d = last_match_data['info']['participants'][part7_index]['deaths']
part8_d = last_match_data['info']['participants'][part8_index]['deaths']
part9_d = last_match_data['info']['participants'][part9_index]['deaths']
part10_d = last_match_data['info']['participants'][part10_index]['deaths']


#Name of all participants champions
part1_c = last_match_data['info']['participants'][part1_index]['championName']
part2_c = last_match_data['info']['participants'][part2_index]['championName']
part3_c = last_match_data['info']['participants'][part3_index]['championName']
part4_c = last_match_data['info']['participants'][part4_index]['championName']
part5_c = last_match_data['info']['participants'][part5_index]['championName']
part6_c = last_match_data['info']['participants'][part6_index]['championName']
part7_c = last_match_data['info']['participants'][part7_index]['championName']
part8_c = last_match_data['info']['participants'][part8_index]['championName']
part9_c = last_match_data['info']['participants'][part9_index]['championName']
part10_c = last_match_data['info']['participants'][part10_index]['championName']


#All participants summoner names
part1_n = last_match_data['info']['participants'][part1_index]['summonerName']
part2_n = last_match_data['info']['participants'][part2_index]['summonerName']
part3_n = last_match_data['info']['participants'][part3_index]['summonerName']
part4_n = last_match_data['info']['participants'][part4_index]['summonerName']
part5_n = last_match_data['info']['participants'][part5_index]['summonerName']
part6_n = last_match_data['info']['participants'][part6_index]['summonerName']
part7_n = last_match_data['info']['participants'][part7_index]['summonerName']
part8_n = last_match_data['info']['participants'][part8_index]['summonerName']
part9_n = last_match_data['info']['participants'][part9_index]['summonerName']
part10_n = last_match_data['info']['participants'][part10_index]['summonerName']


#All participants damage to champions
part1_dmg = last_match_data['info']['participants'][part1_index]['totalDamageDealtToChampions']
part2_dmg = last_match_data['info']['participants'][part2_index]['totalDamageDealtToChampions']
part3_dmg = last_match_data['info']['participants'][part3_index]['totalDamageDealtToChampions']
part4_dmg = last_match_data['info']['participants'][part4_index]['totalDamageDealtToChampions']
part5_dmg = last_match_data['info']['participants'][part5_index]['totalDamageDealtToChampions']
part6_dmg = last_match_data['info']['participants'][part6_index]['totalDamageDealtToChampions']
part7_dmg = last_match_data['info']['participants'][part7_index]['totalDamageDealtToChampions']
part8_dmg = last_match_data['info']['participants'][part8_index]['totalDamageDealtToChampions']
part9_dmg = last_match_data['info']['participants'][part9_index]['totalDamageDealtToChampions']
part10_dmg = last_match_data['info']['participants'][part10_index]['totalDamageDealtToChampions']


#Dictionary with participants names and their champions
part_dmg = {part1_n : part1_dmg, part2_n : part2_dmg, part3_n : part3_dmg, part4_n : part4_dmg,
            part5_n : part5_dmg, part6_n : part6_dmg, part7_n : part7_dmg, part8_n : part8_dmg,
            part9_n : part9_dmg, part10_n : part10_dmg}


#Return max value from part_dmg
max_dmg = max(part_dmg.values())


#Prevents Zero division error in calculating KDA if a player had 0 deaths
if part1_d == 0:
    part1_kda = (part1_k + part1_a)
else:
    part1_kda = (part1_k + part1_a) / part1_d
if part2_d == 0:
    part2_kda = (part2_k + part2_a)
else:
    part2_kda =(part2_k + part2_a) / part2_d
if part3_d == 0:
    part3_kda = (part3_k + part3_a)
else:
    part3_kda = (part3_k + part3_a) / part3_d
if part4_d == 0:
    part4_kda = (part4_k + part4_a)
else:
    part4_kda =(part4_k + part4_a) / part4_d
if part5_d == 0:
    part5_kda = (part5_k + part5_a)
else:
    part5_kda =(part5_k + part5_a) / part5_d
if part6_d == 0:
    part6_kda = (part6_k + part6_a)
else:
    part6_kda =(part6_k + part6_a) / part6_d
if part7_d == 0:
    part7_kda = (part7_k + part7_a)
else:
    part7_kda =(part7_k + part7_a) / part7_d
if part8_d == 0:
    part8_kda = (part8_k + part8_a)
else:
    part8_kda = (part8_k + part8_a) / part8_d
if part9_d == 0:
    part9_kda = (part9_k + part9_a)
else:
    part9_kda = (part9_k + part9_a) / (part9_d)
if part10_d == 0:
    part10_kda = (part10_k + part10_a)
else:
    part10_kda = (part10_k + part10_a) / (part10_d)


#All participants names and kda in dictionary
kda_dict = {part1_n : part1_kda, part2_n : part2_kda, part3_n : part3_kda,
            part4_n : part4_kda, part5_n : part5_kda, part6_n : part6_kda,
            part7_n : part7_kda, part8_n : part8_kda, part9_n : part9_kda,
            part10_n : part10_kda}


#Return max kda
kda_mvp_value = max(kda_dict.values())


#Function for getting kda mvp name and kda value
def find_key_by_value(kda_mvp, value):
    for key, val in kda_mvp.items():
        if val == value:
            return key
    return None

key_by_value1 = find_key_by_value(kda_dict, kda_mvp_value)
kda_mvp = key_by_value1
mvp_kda = kda_mvp_value


#Checks what champion kda_mvp played
if kda_mvp == part1_n:
    kda_mvp_champ = part1_c
elif kda_mvp == part2_n:
    kda_mvp_champ =  part2_c
elif kda_mvp == part3_n:
    kda_mvp_champ= part3_c
elif kda_mvp == part4_n:
    kda_mvp_champ = part4_c
elif kda_mvp == part5_n:
    kda_mvp_champ = part5_c
elif kda_mvp == part6_n:
    kda_mvp_champ = part6_c
elif kda_mvp == part7_n:
    kda_mvp_champ = part7_c
elif kda_mvp == part8_n:
    kda_mvp_champ = part8_c
elif kda_mvp == part9_n:
    kda_mvp_champ = part9_c
else:
    kda_mvp_champ = part10_c



#Function for getting damage mvp name and players damage form part_dmg dict
def find_key_by_value2(part_dmg, value):
    for key, val in part_dmg.items():
        if val == value:
            return key
    return None

key_by_value2 = find_key_by_value2(part_dmg, max_dmg)
dmg_mvp = key_by_value2
mvp_dmg = max_dmg


#Checks wich player is mvp and ads their champion to dm_mvp_champ
if dmg_mvp == part1_n:
    dmg_mvp_champ = part1_c
elif dmg_mvp == part2_n:
    dmg_mvp_champ = part2_c
elif dmg_mvp == part3_n:
    dmg_mvp_champ = part3_c
elif dmg_mvp == part4_n:
    dmg_mvp_champ = part4_c
elif dmg_mvp == part5_n:
    dmg_mvp_champ = part5_c
elif dmg_mvp == part6_n:
    dmg_mvp_champ = part6_c
elif dmg_mvp == part7_n:
    dmg_mvp_champ = part7_c
elif dmg_mvp == part8_n:
    dmg_mvp_champ = part8_c
elif dmg_mvp == part9_n:
    dmg_mvp_champ = part9_c
else:
    dmg_mvp_champ = part10_c


#Checks if participants have same teamid as player and sorts their names and champions into lists myteam_names and myteam_champions
myteam_names = []
myteam_champions = []

if idparticipant1 == my_teamid:
    myteam_names.append(part1_n)
    myteam_champions.append(part1_c)
if idparticipant2 == my_teamid:
    myteam_names.append(part2_n)
    myteam_champions.append(part2_c)
if idparticipant3 == my_teamid:
    myteam_names.append(part3_n)
    myteam_champions.append(part3_c)
if idparticipant4 == my_teamid:
    myteam_names.append(part4_n)
    myteam_champions.append(part4_c)
if idparticipant5 == my_teamid:
    myteam_names.append(part5_n)
    myteam_champions.append(part5_c)
if idparticipant6 == my_teamid:
    myteam_names.append(part6_n)
    myteam_champions.append(part6_c)
if idparticipant7 == my_teamid:
    myteam_names.append(part7_n)
    myteam_champions.append(part7_c)
if idparticipant8 == my_teamid:
    myteam_names.append(part8_n)
    myteam_champions.append(part8_c)
if idparticipant9 == my_teamid:
    myteam_names.append(part9_n)
    myteam_champions.append(part9_c)
if idparticipant10 == my_teamid:
   myteam_names.append(part10_n)
   myteam_champions.append(part10_c)


#Removes player from my team so there's only my teamates
for i in myteam_names:
    if i == summoner_name:
        myteam_names.remove(summoner_name)


#Formating queueid to display queue name
queue_type = ""

if queueid == 440:
    queue_type = "Ranked Flex"
elif queueid == 420:
    queue_type = "Ranked Solo/Duo"
elif queueid == 430:
    queue_type = "Normal Blind Pick"
elif queueid == 400:
    queue_type = "Normal Draft Pick"
elif queueid == 450:
    queue_type = "ARAM Match"
elif queueid == 700:
    queue_type = "Clash Match"
elif queueid == 1090:
    queue_type = "Teamfight Tactics Match"
elif queueid == "custom":
    queue_type = "Custom Game Mach"
else: 
    queue_type = "Queue type not found"


#Calculation of game duration
seconds = gameduration
minutes, remaining_seconds = divmod(seconds, 60)
duration = str(minutes) + ":" + str(remaining_seconds)


#Player's data
champion = last_match_data['info']['participants'][part_index]['championName']
kills = last_match_data['info']['participants'][part_index]['kills']
assists = last_match_data['info']['participants'][part_index]['assists']
deaths = last_match_data['info']['participants'][part_index]['deaths']
minions = last_match_data['info']['participants'][part_index]['totalMinionsKilled']
win = last_match_data['info']['participants'][part_index]['win']
dmg = last_match_data['info']['participants'][part_index]['totalDamageDealtToChampions']
role = last_match_data['info']['participants'][part_index]["role"]
lane = last_match_data['info']['participants'][part_index]["lane"]
gold = last_match_data['info']['participants'][part_index]["goldEarned"]
vision_score = last_match_data['info']['participants'][part_index]["visionScore"]


#Removes champion from my team champions
for i in myteam_champions:
    if i == champion:
        myteam_champions.remove(champion)


#Calculation of player's KDA and preventing ZeroDivisionError
kda = 0
if deaths == 0:
    kda = kills + assists
else:
    kda = (kills + assists) / deaths
    kda = round(kda, 2)


#Calculation and rounding GPM (gold per minute)
gpm = gold / (seconds / 60)
gpm = round(gpm, 2)


#Calculation and rounding MPM (minions per minute)
mpm = minions / ((seconds/60))
mpm = round(mpm, 2)


#Player's items
item0 = last_match_data['info']['participants'][part_index]["item0"]
item1 = last_match_data['info']['participants'][part_index]["item1"]
item2 = last_match_data['info']['participants'][part_index]["item2"]
item3 = last_match_data['info']['participants'][part_index]["item3"]
item4 = last_match_data['info']['participants'][part_index]["item4"]
item5 = last_match_data['info']['participants'][part_index]["item5"]
item6 = last_match_data['info']['participants'][part_index]["item6"]


#Formating items into strings
item0 = str(item0)
item1 = str(item1)
item2 = str(item2)
item3 = str(item3)
item4 = str(item4)
item5 = str(item5)
item6 = str(item6)


#API URL for all items
items_url = "http://ddragon.leagueoflegends.com/cdn/13.16.1/data/en_US/item.json"


#Json with all items
resp5 = requests.get(items_url)
items_numbers = resp5.json()


#Formating win to be a string
if win is True:
    win = 'Win'
else:
    win = "Lose"


#Getting item names, checking if item slot was empty and formating to display empty slot (formating item6 to be a trinket)
try:
    item0 = items_numbers['data'][item0]['name']
except KeyError:
    item0 = "Empty slot"
try:
    item1 = items_numbers['data'][item1]['name']
except KeyError:
    item1 = "Empty slot"
try:
    item2 = items_numbers['data'][item2]['name']
except KeyError:
    item2 = "Empty slot"
try:
    item3 = items_numbers['data'][item3]['name']
except KeyError:
    item3 = "Empty slot"
try:
    item4 = items_numbers['data'][item4]['name']
except KeyError:
    item4 = "Empty slot"
try:
    item5 = items_numbers['data'][item5]['name']
except KeyError:
    item5 = "Empty slot"
try:
    trinket = items_numbers['data'][item6]['name']
except KeyError:
    trinket = "Empty slot"


#Final tuple with all data we want to get
final_list = (matchid, duration, queue_type, win,champion, lane,role, minions,
            mpm, gold, gpm, kills, assists, deaths, kda, dmg, vision_score,
            item0 ,item1, item2, item3, item4, item5, trinket, kda_mvp, mvp_kda,
            kda_mvp_champ, dmg_mvp, mvp_dmg, dmg_mvp_champ)

#print(final_list)

