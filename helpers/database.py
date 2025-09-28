import os
import psycopg


def get_connection():
    conn = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    return conn

def insert_document(content: str, embedding: list[float], conn):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
            (content, embedding),
        )
    conn.commit()


def fetch_similar_documents(query_embedding: list[float], k: int, conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT content, embedding
            FROM documents
            ORDER BY embedding <-> %s::vector
            LIMIT %s
            """,
            (query_embedding, k),
        )
        results = cur.fetchall()
    return results
