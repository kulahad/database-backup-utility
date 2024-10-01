from services import (
    DatabaseService,
    MongoDBService,
    MSSQLService,
    PostgresDBService,
)

from services.mysqlservice import MySQLService

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv

config = dotenv_values(".env")


class ServiceFactory:
    def create(self) -> DatabaseService:
        self.checkdatabasecreds()
        dbtype = os.environ.get("DBTYPE").lower()
        match dbtype:
            case "mongo":
                return MongoDBService()
            case "msql":
                return MySQLService()
            case "mssql":
                return MSSQLService()
            case "postgres":
                return PostgresDBService()
            case _:
                raise TypeError("Invalid db type")

    def checkdatabasecreds(self):
        for item in config:
            if config[item] == "":
                raise KeyError("Missing key from .env file")
