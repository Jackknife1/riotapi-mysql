#Import mysql.connector for connecting to database
import mysql.connector

#Parameters for connection to database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "LOL1v1hra",
    database = "league_of_legends"
)


#Connects to database 
mycursor = connection.cursor()


#Variables from riot_api_data
import riot_api_data
matchid = riot_api_data.matchid
final_list = riot_api_data.final_list


#Check if matchid is already in database
query = "SELECT COUNT(matchid) FROM matches WHERE matchid = %s"
mycursor.execute(query, (matchid,))


#Checks if result is greater than one. If it is, inserts final list into database 
result = mycursor.fetchone()
if not result [0] > 0:
    sql = """
    INSERT INTO matches 
    (Matchid, Duration, Queue_type, Win, Champion, Lane, Role, Minions, MPM, Gold, GPM, Kills, Asissts, Deaths, KDA, 
    Damage, Vision_score, item1, item2, item3, item4, item5, item6, trinket, kda_mvp, mvp_kda, kda_mvp_champion, dmg_mvp, mvp_dmg, dmg_mvp_champion) VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); 
    """
    mycursor.execute(sql, final_list)
    connection.commit()
    
else:
    print("Matchid already in database")


