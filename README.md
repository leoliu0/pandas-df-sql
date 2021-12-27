# pdsql
perform SQL operations on pandas dataframe

A thin wrapper around the wonderful duckdb library i.e. https://duckdb.org/

## Installation
```
pip install pandas-df-sql
```

## Usage
```python
import pandas as pd
import pdsql
test_df = pd.DataFrame.from_dict({"i":[1, 2, 3, 4], "j":["one", "two", "three", "four"]})

pdsql.query("SELECT * FROM test_df where i>2",globals()) # returns a result dataframe
```

It takes two arguments and one optional argument
```python
pdsql.query(query,namespace,disk=False) # returns a result dataframe
```

The ```query``` is a string containing the SQL query to be executed. Currently
only SELECT statement is supported. The ```namespace``` is
a dictionary containing dataframes, It passed ```globals()``` by default. The ```disk``` 
argument is a boolean. By default, a in-memory database is created. if disk set
to True, a disk-based database is created. It is useful when resulting
dataframe is too large to fit in memory.

