from pymongo import MongoClient
import os
import sys
from dotenv import load_dotenv

load_dotenv()
class Database:
    def __init__(self):
        self.__client = None

    def connection(self):
        try:
            self.__client = MongoClient("mongodb+srv://" + os.getenv("MONGODB_USERNAME") + \
                                 ":" + os.getenv("MONGODB_PASSWORD") + \
                                 "@" + os.getenv("MONGODB_DOMAIN") + \
                                 "/" + os.getenv("MONGODB_DBNAME") + "?retryWrites=true&w=majority")
            self.__client.server_info()
            return self.__client
        except Exception as e:
            with open('readme.txt', 'w') as f:
                f.write(str(e))
                f.write('\n')
                f.close()
            script = "./mail_report.sh \"ERROR CONNECTION TO DATABASES\""
            os.system(script)
            sys.exit(0)
