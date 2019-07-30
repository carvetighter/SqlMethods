from SqlMethods import SqlMethods
import pymssql

# iterators
list_up = [r'Frosty-SB-02\FROSTY SB 02', r'suM~=EqNV\D1']

# attempt 00
list_00 = list(list_up)
list_00.insert(1, r'localhost\SQLEXPRESS')
list_00.append(r'Dev_Env')
sql_conn_00 = SqlMethods(list_00)
print('sql_conn_00: %s' %sql_conn_00.bool_is_connected)

# attempt 01
list_01 = list(list_up)
list_01.insert(1, r'frosty-sb-02\SQLEXPRESS')
list_01.append(r'Dev_Env')
sql_conn_01 = SqlMethods(list_00)
print('sql_conn_01: %s' %sql_conn_01.bool_is_connected)

# attempt 02
string_server = r'localhost\SQLEXPRESS'
string_db = r'Dev_Env'
string_user = r'Frosty-SB-02\Frosty SB 02'
string_pswd = r'suM~=EqNV\D1'
psql_conn = pymssql.connect(string_server, string_user, string_pswd, string_db)