import sqlite3

con = sqlite3.connect("TMA.db")

cur = con.cursor()

cur.execute("""

    CREATE TABLE IF NOT EXISTS answers(
            id INTEGER,
            question_id INTEGER,
            answer TEXT)
            """
            )


cur.execute("""

    INSERT INTO answers VALUES
            (1, 101, "THE answer is 42"),
            (2, 102, "The answer is 100");
            """
            )

cur.execute("SELECT * from answers")


con.commit()
result = cur.fetchall()
print(result)


