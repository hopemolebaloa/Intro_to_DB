import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL Server (Update credentials if necessary)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Explicitly handling MySQL errors
        print(f"Error: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
