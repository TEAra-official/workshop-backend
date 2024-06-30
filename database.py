import sqlite3
con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE user
               (name text, age real, school text, comment text)''')

# Insert a row of data
cur.execute("INSERT INTO user VALUES ('tori','23','お茶情','TEAraの運営をしています。')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
