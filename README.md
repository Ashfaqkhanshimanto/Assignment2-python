[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BPC-P9Ij)
# tpl-xaml-python-fall-2024-assignment-2

## Steps

### Database Setup

Create a database setup script, that can be run to create and setup the database and database table.

1. **Use sqlite3 or SQLAlchemy to create an SQLite database named countries.db.**
2. **Create a table named Countries with columns id, country_name, area and population.**
   - Ensure that each entry has a unique id.
   - Notice the data type you set for the fields, numbers should be integers etc.

Refer to the material, there should be enough information to get this done.

### Save Country Data

Create a data ingestion script, which handles reading data from its origin (csv file) and saving the data to database.

3. **Read the data from the coutries.csv file.**
4. **Insert the country data into the Countries database table.**

### Query and visualize the data

Create a data visualization script, that reads the data from database and visualizes it.

A function most_populated that does

5. **an SQL query to retrieve the 20 most populated countries from the Countries table.**
6. **a bar plot of the data.**

A function largest_area function that does

7. **an SQL query to retrieve 10 countries with the larges land area from the Countries table.**
8. **a bar plot of the data.**

Use matplotlib or seaborn to create the bar plots.
Set the x-axis to display country names and the y-axis to display the other values.
