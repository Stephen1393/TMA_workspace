import sqlite3


def get_connection():
    return sqlite3.connect("TMA.db")

def get_answers():
    con = get_connection()

    cur = con.cursor()

    cur.execute("SELECT * FROM answers")

    result = cur.fetchall()

    con.close()
    
    return result


def get_answer(question_id):
    con = get_connection()

    cur = con.cursor()

    cur.execute(
            "SELECT * FROM answers WHERE question_id = ?",

            (question_id,)

            )

    result = cur.fetchone()

    con.close()

    return result



