import psycopg2
import config

try:
    connection = psycopg2.connect(host="localhost", database=config.db["db"], user=config.db["username"], password=config.db["password"])

    createTable = """
        DROP TABLE IF EXISTS lexemes;
        CREATE TABLE lexemes
        (
            id SERIAL PRIMARY KEY NOT NULL,
            class CHAR(4) NOT NULL,
            word CHAR(30) NOT NULL,
            inflgroup INT,
            av CHAR(1),
            keywords CHAR(30)[],
            keysentence CHAR(200)
        );
    """
    connection.cursor().execute(createTable)
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
