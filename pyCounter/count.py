import re

# pattern = re.compile(r'\n*\* (\w*)\n')
#errorClassesDict = {'mysql','duplicateFunctionParameter','arrayValueByReference','magic_quotes_runtime','list','ereg','split','oldClassConstructors','static','variableInterpolation','foreachByReference','arrayValueByReference','newOperatorWithReference','pregEval'}
pattern = re.compile(r'(mysql|duplicateFunctionParameter|arrayValueByReference|magic_quotes_runtime|invalidList|ereg|split|oldClassConstructors|static|variableInterpolation|foreachByReference|arrayValueByReference|newOperatorWithReference|pregEval)')
pattern_mysql = re.compile(r'(mysql_affected_rows|mysql_client_encoding|mysql_close|mysql_connect|mysql_create_db|mysql_data_seek|mysql_db_name|mysql_db_query|mysql_drop_db|mysql_errno|mysql_error|mysql_escape_string|mysql_fetch_array|mysql_fetch_assoc|mysql_fetch_field|mysql_fetch_lengths|mysql_fetch_object|mysql_fetch_row|mysql_field_flags|mysql_field_len|mysql_field_name|mysql_field_seek|mysql_field_table|mysql_field_type|mysql_free_result|mysql_get_client_info|mysql_get_host_info|mysql_get_proto_info|mysql_get_server_info|mysql_info|mysql_insert_id|mysql_list_dbs|mysql_list_fields|mysql_list_processes|mysql_list_tables|mysql_num_fields|mysql_num_rows|mysql_pconnect|mysql_ping|mysql_query|mysql_real_escape_string|mysql_result|mysql_select_db|mysql_set_charset|mysql_stat|mysql_tablename|mysql_thread_id|mysql_unbuffered_query|mcrypt_generic_end|mcrypt_ecb|mcrypt_cbc|mcrypt_cfb|mcrypt_ofb|set_magic_quotes_runtime|magic_quotes_runtime|set_socket_blocking)\(')
#linePattern = '\* deprecatedFunctions(\s.*\n)+\n'
count = {}
count_mysql = {}

# add found errorClasses to Dict. If already present, increase counter
def addToDict(errorClass, dictToSave):
    if errorClass in dictToSave:
        dictToSave[errorClass] += 1
    else:
        dictToSave[errorClass] = 1

# helper to print dictionary
def prettyPrint(dictToPrint):
    for key in dictToPrint:
        print(f'{key}: {dictToPrint[key]}')

with open('report.md', 'r') as file:
    text = file.read()
    data = re.findall(pattern, text)
    data_mysql = re.findall(pattern_mysql, text)
    for errorClass in data:
        addToDict(errorClass, count)
    for errorClass in data_mysql:
        addToDict(errorClass, count_mysql)
    prettyPrint(count)
    prettyPrint(count_mysql)

