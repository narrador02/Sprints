from mysql import connector

class Connection:
    _connection = None

    @staticmethod
    def connect():
        Connection._connection = connector.connect(
            host="localhost",
            user="admin",
            password="password",
            database="schoolControl"
        )

    @staticmethod
    def get():
        if not Connection._connection:
            Connection.connect()
        return Connection._connection

    @staticmethod
    def close():
        if Connection._connection:
            Connection._connection.close()
            Connection._connection = None