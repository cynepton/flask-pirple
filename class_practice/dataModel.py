import sqlite3

def show_color(username):
    """
    docstring
    """
    connection = sqlite3.connect("pirple_t.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT favorite_colorFROM users
        WHERE username='{username}'
        ORDER BY pk DESC;""".format(username=username))
    color = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message = "{username}'s favorite color is {color}".format(username=username, color=color)
    return message