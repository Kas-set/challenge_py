import sqlite3
#connexion 

con = sqlite3.connect("albums.db")

curseur = con.cursor()

# curseur.execute(
#     """CREATE TABLE artistes(
#         artist_id INTEGER  PRIMARY KEY AUTOINCREMENT,
#         nom VARCHAR(30) NOT NULL        
#         )
#    """)
# curseur.execute(
#     """INSERT INTO artistes(nom) VALUES("Michael Jackson");
#     """
# )
curseur.execute(
    """ SELECT * FROM artistes;
    """
)
artistes = curseur.fetchall()
print(artistes
      )
con.commit()
curseur.close()
