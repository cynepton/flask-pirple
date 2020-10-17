import sqlite3

def show_color(username):
    """
    docstring
    """
    connection = sqlite3.connect("pirple_t.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT favorite_color FROM users
        WHERE username='{username}'
        ORDER BY pk DESC;""".format(username=username))
    color = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()
    message = "{username}\'s favorite color is {color}.".format(username=username, color=color)
    return message

def check_password(username):
    """
    """
    connection = sqlite3.connect("pirple_t.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT password FROM users
        WHERE username = '{username}'
        ORDER BY pk DESC;""".format(username=username)
        )
    password = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()
    return password