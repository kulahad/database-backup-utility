from abc import abstractmethod, ABC


class DatabaseService(ABC):
    def __init__(self) -> None:
        pass

    abstractmethod

    def connector(self):
        pass

    abstractmethod

    def backup(self):
        pass

    abstractmethod

    def restore(self):
        pass

    abstractmethod

    def compress(self):
        pass

    abstractmethod

    def logger(self):
        pass


# TODO: Move classes to different files, implement connection, logger


class MongoDBService(DatabaseService):
    def connector(self):

        return super().connector()

    def backup(self):
        print("Backing up from mongodb!")


class PostgresDBService(DatabaseService):
    def backup(self):
        print("Backing up from postgres!")


class MSSQLService(DatabaseService):
    def backup(self):
        print("Backing up from mssql!")
