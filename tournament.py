import psycopg2


def connect():
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Cannot connect!")


def deleteMatches():
    db = connect()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE match CASCADE")
    db.commit()
    db.close()


def deletePlayers():
    db = connect()
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE Player CASCADE")
    db.commit()
    db.close()

def countPlayers():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM Player")
    count = cursor.fetchone()[0]
    db.close()
    return count


def registerPlayer(name):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO Player(name) VALUES(%s)"
    cursor.execute(query, (name, ))
    db.commit()
    db.close()


def playerStandings():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT p_id AS id, name, (SELECT COUNT(w_id)"
              "FROM match where w_id = p_id) as wins,"
              "(SELECT COUNT(m_id) from match where w_id = "
              "p_id or l_id = p_id) as match from Player "
              "GROUP BY p_id ORDER BY wins DESC")
    result = cursor.fetchall()
    db.close()
    return result


def reportMatch(winner, loser):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO match(w_id, l_id) VALUES(%s, %s)"
    para = (winner,loser, )
    cursor.execute(query,para)
    db.commit()
    db.close()

def swissPairings():
    result = playerStandings()
    list1 = []
    count = len(result)
    for i in range(0, count - 1, 2):
        pairing = (result[i][0], result[i][1],
                   result[i+1][0], result[i+1][1])
        list1.append(pairing)
    return list1
