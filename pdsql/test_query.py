import pandas as pd
from ._main import query

def test_query():
    global test_df
    test_df = pd.DataFrame.from_dict({"i":[1, 2, 3, 4], "j":["one", "two", "three", "four"]})
    assert (query('SELECT * FROM test_df',globals())==test_df).all().all()
