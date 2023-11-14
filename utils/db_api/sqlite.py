import sqlite3


class Database:
    def __init__(self, path_to_db="D:/azamat_all/MY AIOGRAM BOTS/Shaxsiy-Bot/data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
        
    def create_table_urls(self):
        sql = """
        CREATE TABLE Urls (
            id INTEGER PRIMARY KEY,
            file_id TEXT NOT NULL,
            link TEXT NOT NULL
            );
"""
        self.execute(sql, commit=True)
            
    def create_table_game(self):
        sql = """
        CREATE TABLE Game (
            id PRIMARY KEY,
            user_id BIGINT NOT NULL,
            winner VARCHAR(50) NOT NULL
    );
"""
        self.execute(sql, commit=True)
        
    def create_table_channels(self):
        sql = """
        CREATE TABLE Channels (
            id PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            channel_id BIGINT NOT NULL UNIQUE,
            username VARCHAR(255)  
    );
"""  
        self.execute(sql, commit=True)
        
    def create_table_groups(self):
        sql = """
        CREATE TABLE Groups (
            id PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            group_id BIGINT NOT NULL UNIQUE,
            username VARCHAR(255)
    );
"""
        self.execute(sql, commit=True)        
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str,language: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, language) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, language), commit=True)
    
    def add_urls(self, file_id: str,link: str):

        sql = """
        INSERT INTO Urls(file_id, link) VALUES(?, ?)
        """
        self.execute(sql, parameters=(file_id, link), commit=True)
        
    def add_game(self, user_id, winner):
        sql = "INSERT INTO Game (user_id, winner) VALUES (?, ?)"
        self.execute(sql, parameters=(user_id, winner,), fetchone=True)
    
    def add_channel(self, title: str,channel_id: int,username: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, title, channel_id, username) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(title, channel_id, username), commit=True)
    
    def add_groups(self, title: str, group_id: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, title, group_id, username)) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(title, group_id), commit=True)
    
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_channels(self):
        sql = """
        SELECT * FROM Channels
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_groups(self):
        sql = """
        SELECT * FROM Groups
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_urls(self):
        sql = """
        SELECT * FROM Urls
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_games(self, **kwargs):
        sql = "SELECT * FROM Game WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def count_channels(self):
        return self.execute("SELECT COUNT(*) FROM Channels;", fetchone=True)
    
    def count_groups(self):
        return self.execute("SELECT COUNT(*) FROM Groups;", fetchone=True)
    
    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def delete_channels(self):
        self.execute("DELETE FROM Channels WHERE TRUE", commit=True)
        
    def delete_groups(self):
        self.execute("DELETE FROM Groups WHERE TRUE", commit=True)

def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
