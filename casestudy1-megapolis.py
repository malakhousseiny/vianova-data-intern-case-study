import pandas as pd
from sqlalchemy import create_engine


#to read the given data set
data = pd.read_csv('geonames-all-cities-with-a-population-1000.csv', sep=';', encoding='latin1')


#To Preprocess the dataset,selecting only the following columns: 'Country Code', 'Country name EN', and 'Population'
#filter the cities whose population > 10,000,000 to remove out of the new dataset
#group the data by 'country code' and 'country name EN'as implied by the case study to get countries that don't host a megapolis
#Sort the data by 'Country name EN'
filtered_data = data[data['Population'] <= 10000000]
grouped_data = filtered_data.groupby(['Country Code', 'Country name EN'], as_index=False).size()
sorted_data = grouped_data.sort_values('Country name EN')

#save the result as a tab-separated value (TSV) file names 'result.tsv'
result = sorted_data[['Country Code', 'Country name EN']]
result.to_csv('result.tsv', sep='\t', index=False)

#setting up a database connection 
engine = create_engine('sqlite:///cities.db')
connection = engine.connect()

#store the dataset in the database
data.to_sql('cities', con=connection, if_exists='replace')

#Perform a query on SQL to retrieve countries that don't host a megapolis
query = '''
SELECT "Country Code", "Country name EN"
FROM cities
WHERE Population <= 10000000
GROUP BY "Country Code", "Country name EN"
ORDER BY "Country name EN"
'''
result = pd.read_sql_query(query, connection)

#Save the SQL query result as a TSV file:
result.to_csv('result.tsv', sep='\t', index=False)

#Close the database connection:
connection.close()

#the result.tsv include some country codes without their corresponding country names as the names were not given in the original dataset 