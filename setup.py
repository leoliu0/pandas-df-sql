#!/usr/bin/python

from setuptools import setup

setup(name='pandas_df_sql',
      version='0.2',
      description='Perform SQL queries on pandas dataframes',
      author='Leo Liu',
      author_email='leo.liu@unsw.edu.au',
      packages=['pdsql',],
      install_requires=[
          'pandas',
          'duckdb',
      ],
     )
