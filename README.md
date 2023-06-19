# Case study


We want to know the __countries that don't host a megapolis__


The purpose of this exercice is to evaluate your skills in Python and SQL. You'll have to fork this repository and write a program that fetch the [dataset of the population of all cities in the world](https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/export/?disjunctive.cou_name_en), stores it in a database, then perform a query that will compute: what are the countries that don't host a megapoliss (a city of more than 10,000,000 inhabitants)? 

The program will save the result (country code and country name) as a tabulated separated value file, ordered by country name. 

You should answer as if you were writting production code within your team. You can imagine that the program will be run automatically every week to update the resulting data.

Please send us the link to your github repository with the answer of the exercise. 

# Countries without Megapolis - Case Study Solution by Malak HOUSSAINI

This project provides a solution for the case study on identifying countries without a megapolis. It is implemented in Python using the Pandas library for data manipulation and SQLite for database management.

## Project Overview

The goal of this project is to analyze a dataset of cities and identify countries that do not have a megapolis, i.e., cities with a population over 10 million. The project involves the following steps:

1. **Environment Setup**: Install the required packages (Pandas and SQLAlchemy) by running the command `conda install pandas sqlalchemy` in Anaconda Prompt.

2. **Fork the Repository**: Fork the original repository to create your own copy.

3. **Code Implementation**: Create a new Python script on any IDE (visual studio in my case) and import the necessary libraries: Pandas and SQLAlchemy.

4. **Data Reading**: Read the provided sample dataset (`geonames-all-cities-with-a-population-1000.csv`) into a Pandas DataFrame.

5. **Data Preprocessing**: Filter the dataset to exclude cities with a population over 10 million. Group the data by country code and name and sort it in ascending order of country name.

6. **Save Results**: Save the sorted and filtered data as a tab-separated value (TSV) file named `result.tsv`.

7. **Database Setup**: Establish a connection to a SQLite database (`cities.db`).

8. **Data Storage**: Store the original dataset in the SQLite database for future reference.

9. **Perform SQL Query**: Execute an SQL query on the database to retrieve the countries without a megapolis. The query groups the data by country code and name and orders it by country name.

10. **Save Query Results**: Save the result of the SQL query as a TSV file named `result.tsv`.

11. **Database Cleanup**: Close the database connection.

12. **Commit and Push**: Commit your code changes and push them to your GitHub repository.

## Running the Project

To run the project, follow these steps:

1. Set up the environment(on anaconda) and install the required packages using the provided command.

2. Fork the repository to create your own copy.

3. Create a new Python script and import the required libraries.

4. Use the code implementation steps mentioned above into your script.

5. Place the `geonames-all-cities-with-a-population-1000.csv` file in the same directory as your script.

6. Run the script.

7. The script will generate the `result.tsv` file, which contains the list of countries without a megapolis.

Deployment:
- This project is intended to be run locally.
- To automate it, you can set up a scheduled task or use the Task Scheduler on your operating system to run the Python scripts periodically, or once in a week to update the result data.

Built With:
- Python 3.x (3.10.11): The programming language used.
- SQLite: The database engine used for storing and querying the data.

Author:
- [Malak HOUSSAINI](https://github.com/malakhousseiny)

License:
- This project is licensed under the MIT License.
