def model(dbt,session):
    dbt.config(materialized="table")
    return session.sql("call emp_table('ACCOUNT')")