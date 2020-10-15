import sqlite3

connection = sqlite3.connect('pirple_t.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
    ) VALUES(
        "Isaac",
        "isaac",
        "Black"
    );
    """
)

connection.commit()
cursor.close()
connection.close()