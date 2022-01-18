"""
Database connection module
"""
from app import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class DBConnection:
    """
    DB connection class
    """

    def __init__(self) -> None:
        """
        Constructor to create connection
        """
        self.__server = config['DB']['SERVER']
        self.__data_base = config['DB']['DATABASE_NAME']
        self.__username = config['DB']['USER_NAME']
        self.__password = config['DB']['PASSWORD']
        self.__conn_str = f"mysql+mysqldb://{self.__username}:{self.__password}@{self.__server}/{self.__data_base}"
        engine_args = {
            'pool_size': 30, 'pool_pre_ping': True, 'max_overflow': 0
        }
        self.__engine = create_engine(self.__conn_str, **engine_args)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)

    def get_session(self) -> object:
        """
        Getting session of database
        """
        BASE.metadata.create_all(self.__engine)
        return self.__session()
