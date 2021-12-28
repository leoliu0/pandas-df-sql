import duckdb
import tempfile
import re
from loguru import logger
import os

def query(query,ns, disk=False):
    """
    This function takes a SQL query as input and returns the results as a dataframe.
    :param db: duckdb.database object
    :param query: SQL query
    :return: dataframe
    """
    try:
        os.remove("tmp.duckdb")
    except:
        pass
    def extract_table_names(query):
        """ Extract table names from an SQL query. """
        # a good old fashioned regex. turns out this worked better than actually parsing the code
        tables_blocks = re.findall(r'(?:FROM|JOIN)\s+(\w+(?:\s*,\s*\w+)*)', query, re.IGNORECASE)
        tables = [tbl
                  for block in tables_blocks
                  for tbl in re.findall(r'\w+', block)]
        return set(tables)
    if disk:
        logger.info(f"using file database tmp.duckdb")
        db = duckdb.connect(database="tmp.duckdb") # On disk
    db = duckdb.connect() # In-memory database
    tables = extract_table_names(query)
    for table in tables:
        db.register(table,ns[table])

    df = db.query(query).df()
    db.close()
    if disk:
        try:
            os.remove("tmp.duckdb")
        except:
            logger.warning("could not delete tmp.duckdb")
    return df
