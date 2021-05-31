import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE sequence (
            seq_key SERIAL PRIMARY KEY,
            value INTEGER NOT NULL
        )
        """

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute(commands)