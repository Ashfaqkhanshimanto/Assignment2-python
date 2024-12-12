import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Database Setup ---
def setup_database():
    """Creates and sets up the countries database and table."""
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            area INTEGER NOT NULL,
            population INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# --- Save Country Data ---
def ingest_data(csv_file):
    """Reads country data from CSV and saves it to the database."""
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()

    # Read data from CSV
    df = pd.read_csv(csv_file)

    # Insert data into the database
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO Countries (name, area, population) 
            VALUES (?, ?, ?)
        ''', (row['name'], row['area'], row['population']))

    connection.commit()
    connection.close()

# --- Query and Visualize Data ---
def most_populated():
    """Retrieves the 20 most populated countries and visualizes them."""
    connection = sqlite3.connect('countries.db')
    query = '''
        SELECT name, population FROM Countries
        ORDER BY population DESC LIMIT 20
    '''
    df = pd.read_sql_query(query, connection)
    connection.close()

    # Plot data
    plt.figure(figsize=(12, 6))
    sns.barplot(x='population', y='name', data=df, palette='viridis')
    plt.title('Top 20 Most Populated Countries')
    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def largest_area():
    """Retrieves the 10 countries with the largest area and visualizes them."""
    connection = sqlite3.connect('countries.db')
    query = '''
        SELECT name, area FROM Countries
        ORDER BY area DESC LIMIT 10
    '''
    df = pd.read_sql_query(query, connection)
    connection.close()

    # Plot data
    plt.figure(figsize=(12, 6))
    sns.barplot(x='area', y='name', data=df, palette='coolwarm')
    plt.title('Top 10 Largest Countries by Area')
    plt.xlabel('Area')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    setup_database()

    #countries.csv
    csv_file = 'countries.csv'
    ingest_data(csv_file)

    # Visualizations
    most_populated()
    largest_area()
