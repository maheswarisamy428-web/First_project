import os
import snowflake.connector

def test_snowflake_connection():
    ctx = snowflake.connector.connect(
        user=os.environ['SNOWFLAKE_USER'],
        password=os.environ['SNOWFLAKE_PASSWORD'],
        account=os.environ['SNOWFLAKE_ACCOUNT'],
        warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
        database=os.environ['SNOWFLAKE_DATABASE'],
        schema=os.environ['SNOWFLAKE_SCHEMA']
    )
    cs = ctx.cursor()
    try:
        cs.execute("SELECT CURRENT_VERSION()")
        version = cs.fetchone()
        print("Snowflake version:", version[0])
    finally:
        cs.close()
        ctx.close()
