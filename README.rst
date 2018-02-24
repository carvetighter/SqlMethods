SqlMethods
-------------------------

| This package is disigned to be a light wight wrapper for pymssql used for Miscrosoft SQL Server.  This
was developed as I was working with Sql Servers to make it easy and quick to do a lot of the 
functionality that would duplicate code for in Data Science my projects.  This is not a comprehensive 
list of functionality but the most popular ones I used.  This version does not support Azure at the 
moment.  That will come in a later version.

Installation
============
``pip install SqlMethods``

Usage
=====
|
| **Connect to the SQL Server:**

Each class instance can only connect to one database.  To connect to multiple databases you will
need multple instances of the class.

::
    from SqlMethods import SqlMethods
    list_args = [r'login name', r'server name', r'passwrod', r'database name']

    sql_srvr = SqlMethods(list_args)
    print(sql_svr.bool_is_connected)

| **Connect to the Sql Server ouput:

::
    True # if connection is established
    # or
    False # if connection is not established

| **Query database:**
| 
| Assuming a connection (sql_srvr) is established.

::
    # simple query
    string_query = 'select top 10 * from dbo.table'
    list_query_results = sql_srvr.query_select(string_query)

| The list returned is a list of length 2.
| list_query_results[0] -> boolean; True or False
| list_query_results[1] -> potentially a multidimensional list of values from the query; in this case the first 10 records
|   if list_query_results[0] is True list_query_results[1] will have the data
|   if list_query_results[0] is False list_query_results[1] will have the error message from the Sql Server
|
| Note: if you are pulling only one column or your results results in a sinlge column of data.  You will
| need to use a list comprehension to be able to add it to a pandas Series.
| 
| example:
::
    list_results_for_series = [x[0] for x in list_query_results[1]]
    series_one_column = pandas.Series(data = list_results_for_series, name = 'column_name')

| If your query reults in more than one column of data you can use the following code to add it to
a pandas datafarme.
|
| example:
::
    list_table_columns = sql_srvr.get_table_columns('table_name')
    if list_table_columns[0] and list_query_results[0]:
        df_sql_query = pandas.DataFrame(data = list_query_results[1], columns = list_table_columns[1])

| continued...
