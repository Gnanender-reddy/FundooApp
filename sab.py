# from models.datamanagement import mydbobj



# def user_insert(self, data, table_name=None):
#         table_name = table_name
#         column = []
#         rows_values = []
#         val = []
#         for key, value in data.items():
#             column.append(key)
#             rows_values.append("%s")
#             val.append(value)
#         column = ', '.join(column)
#         val_ = ', '.join(['%s'] * len(val))
#         print(column)
#         print(rows_values)
#         print(val)
#         query = '''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
#         print(query)
#         mydbobj.execute(query=query, value=val)

def read(data,table_name=None):
    table_name=table_name
    column=[]
    rows=[]
    val=[]
    for key,value in data.items():
        column.append(key)
        rows.append("%s")
        val.append(value)
