import psycopg2


def create_table():
    # Connect to the database
    conn = psycopg2.connect("host=localhost dbname=application user=postgres password=mypassword")

    # Create a cursor
    cur = conn.cursor()

    # Create the table
    #cur.execute("CREATE TABLE Firsttable (name VARCHAR(255))")
    cur.execute("INSERT INTO Firsttable values ('vivek')")

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


# Call the create_table() function
create_table()
