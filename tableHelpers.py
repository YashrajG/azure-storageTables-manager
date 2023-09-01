from pandas import DataFrame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DAO import SampleTable

# Required for setting up azuretables dialect in sqlalchemy
# from sqlalchemy.dialects import registry
# registry.register('azuretables', 'dialect')

class tableDMLHelper:

    def __init__(self, tableName: str, accountName: str, accountKey: str) -> None:
        self.accountName = accountName
        self.accountKey = accountKey

        self.tableName = tableName
        self.tableDAO = tableDMLHelper.getTableDAO(tableName)

    @staticmethod
    def getTableAccessSession(accountName: str, accountKey: str):
        engine = create_engine(f"azuretables:///?AccessKey={accountKey}&Account={accountName}")
        factory = sessionmaker(bind=engine)
        session = factory()
        return session
    
    @staticmethod
    def getTableDAO(tableName: str):
        if tableName == 'SampleTable':
            return SampleTable.metadata.tables[tableName]
        else:
            return None
    
    def readData(self):
        session = tableDMLHelper.getTableAccessSession(self.accountName, self.accountKey)
        queryResult = session.execute(self.tableDAO.select())
        df = DataFrame(queryResult.fetchall())
        return df