from services import DatabaseService


class MySQLService(DatabaseService):
    def backup(self):
        print("Backing up from mysql!")

    def restore(self):
        # check if variables are loaded or not

        return super().restore()
