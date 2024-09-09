import mysql.connector

tables = {
    'agendanotes': ['idNotes','note', '_date', 'details']
}
 
class MySQLConnection():
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = None
        
    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )

        except Exception as err:
            print('no se estableció la conexión')
    
    def disconnect(self):
        if (self.mydb.is_connected()):
            self.mydb.close()
        
    def select(self, table):
        query = f"SELECT * FROM {table}"

        cursor = self.mydb.cursor()
        cursor.execute(query)

        return cursor.fetchall()
        
    def insert(self, table, values):
        columns = ''
        insert_values = []
        insert_values_type = ''


        for i in tables[table][1:]:
            columns += f'{i}, '

        columns = columns[:-2]

        for data in values:
            insert_values_type += f"{data[1]}, "
            insert_values.append(data[0])

        insert_values_type = insert_values_type[:-2]

        query = f"INSERT INTO {table} ({columns}) VALUES ({insert_values_type})"

        cursor = self.mydb.cursor()
        cursor.execute(query, insert_values)

        self.mydb.commit()

    def delete(self, table, id):
        query= f'DELETE FROM {table} WHERE {tables[table][0]} = {id}'

        cursor = self.mydb.cursor()

        cursor.execute(query)
        
        self.mydb.commit()

    def update(self, table, id, values):
        str_values = ''
        aux_table = tables[table]
        insert_values = []

        for i in range(len(values)):
            str_values += f'{aux_table[i+1]} = {values[i][1]}, '
            insert_values.append(values[i][0])

        str_values = str_values[:-2]

        query= f'UPDATE {table} SET {str_values} WHERE {aux_table[0]} = {id}'

        cursor = self.mydb.cursor()

        cursor.execute(query, insert_values)

        self.mydb.commit()


