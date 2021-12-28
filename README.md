# pdsql
perform SQL operations on pandas dataframe

A thin wrapper around the wonderful duckdb library i.e. https://duckdb.org/

## Installation
```
pip install -U pandas-df-sql
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
a dictionary containing dataframes, one can simply pass ```globals()```. The ```disk``` 
argument is a boolean. By default, a in-memory database is created. if disk set
to True, a disk-based database is created. It is useful when resulting
dataframe is too large to fit in memory.

## Why?
pandasql is fantastic, but too slow for big datasets. To use SQL, one needs to load pandas df into a SQLITE database and query the data back into pandas, incur a huge IO cost. duckdb transfer data very efficiently between itself and pandas, so it is way faster. Recently, the technology develops around apache arrow aiming at zero-copying
https://duckdb.org/2021/12/03/duck-arrow.html

Other SQL-mimicking technologies such as IBIS are not as feature rich as a real SQL database. One would want a complete SQL experience.
