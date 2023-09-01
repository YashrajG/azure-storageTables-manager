import pandas
from tableHelpers import tableDMLHelper

TABLE_NAME = 'sampleData'
ACCOUNT_NAME = 'incedoyashtabledata'
ACCOUNT_KEY = ''

# Sample Table Management
promptsTable = tableDMLHelper(TABLE_NAME, ACCOUNT_NAME, ACCOUNT_KEY)

# Returns a Pandas Dataframe
promptsDF = promptsTable.readData()
promptsDF.head(5)