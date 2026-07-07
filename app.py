import sqlite3


def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerável propositalmente para teste do Copilot ok
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    conn.close()
    return user


if __name__ == "__main__":
    login("admin", "123456")

#command