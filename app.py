import sqlite3


def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerável propositalmente para teste do Copilot ok ok
    query = (
        f"SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user


if __name__ == "__main__":
    login("admin", "123456")