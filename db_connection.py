import psycopg2  

try:
     # connect to database
    con = psycopg2.connect(user = "marco",
                                  password = "marcotest",
                                  host = "127.0.0.1",
                                  port = "5432",
                                 database = "SpoonRiver[IT]")

    cur = con.cursor()
    con.autocommit=True

 
    # Print PostgreSQL version
    cur.execute("SELECT version();")

    record = cur.fetchone()
    print("\nYou are connected to - ", record,"\n")


    cur.execute("SELECT current_database();")

    record = cur.fetchone()
    print("\nYou're connected to: - ", record,"\n")

    cur.execute("CREATE TABLE IF NOT EXISTS POESIA (ID SERIAL, TESTO TEXT NOT NULL);")

    def inserisciPoesia(poesia,id):
        print("Inizio inserimento:")
        cur.execute("INSERT INTO poesia (id, testo) VALUES(%s, %s)", (id,poesia))
        con.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into table poesia")


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(con):
       print("PostgreSQL connection is closed")