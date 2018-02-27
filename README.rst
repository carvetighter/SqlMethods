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
| **Connect to the SQL Server:**

Each class instance can only connect to one database.  To connect to multiple databases you will
need multple instances of the class.

::

    from SqlMethods import SqlMethods
    list_args = [r'login name', r'server name', r'passwrod', r'database name']

    sql_srvr = SqlMethods(list_args)
    print(sql_svr.bool_is_connected)

| **Connect to the Sql Server ouput**:

::

    True # if connection is established
    # or
    False # if connection is not established

| **Query database:**
| Assuming a connection (sql_srvr) is established.

::

    # simple query
    string_query = 'select top 10 * from dbo.table'
    list_query_results = sql_srvr.query_select(string_query)

| The list returned is a list of length 2.
|
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
| a pandas datafarme.
|
| example:
::

    list_table_columns = sql_srvr.get_table_columns('table_name')
    if list_table_columns[0] and list_query_results[0]:
        df_sql_query = pandas.DataFrame(data = list_query_results[1], columns = list_table_columns[1])

| **Insert into database:**
| Before you insert it is a good idea to check if the table is created.  The below example illistrates how
| to insert into the table and check if the table is created.
|
| example (check table or create):
::

    bool_table_exists = sql_srvr.table_exists(string_table_name)
    if not bool_table_exists:
        list_create_table = sql_srvr.create_table(string_table_name, 
                                ['int_id int', 'date_record datetime', 'string_customer varchar(100)'])
        bool_table_exists = list_create_table[0]
    
| The columns are in a list with the column name and data type.  The when the table is created
| the data compression is enable and the table is a narrow table (1,024 columns or less).
|
| When inserting into the table the method will determine if you are inerting one value or more than
| by the lenght of the list of values.  This needs to be a list of lists.  An easy way to convert a pandas
| dataframe is to use the following line of code:
::
    
    list_insert = df_sql_query.values.tolist()

| The following example will insert into the table created above:
::

    if bool_table_exists:
        list_insert_results = sql_srvr.insert(string_table_name, list_table_columns, 
                                df_sql_query.values.tolist())

| The method will insert 100,000 records at a time.  In ``list_insert_results`` the format is the same
| as ``list_query_results``.  The first value is a boolean determining if the insert completed with no
| errors.  The second values will be an empy list of the first value is ``True``.  If the first value is 
| ``False`` then the error message will be in the second postion of the list.
