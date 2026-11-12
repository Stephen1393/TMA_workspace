import sqlite3


def get_connection(database: str = "TMA.db"):
    return sqlite3.connect(database)

def get_answers(database: str = "TMA.db"):
    con = get_connection(database)

    cur = con.cursor()

    cur.execute("SELECT * FROM answers")

    result = cur.fetchall()

    con.close()
    
    return result


def get_answer(question_id: int, database: str = "TMA.db"):
    con = get_connection(database)

    cur = con.cursor()

    cur.execute(
            "SELECT * FROM answers WHERE question_id = ?",

            (question_id,)

            )

    result = cur.fetchone()

    con.close()

    return result



