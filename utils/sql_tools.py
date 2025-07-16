import os
from sqlalchemy import create_engine, inspect
from urllib.parse import quote_plus
from sqlalchemy.exc import OperationalError


def create_sqlalchemy_engine(env_vars, docker_mode=False):
    try:
        user = env_vars.get("MYSQL_USER")
        password_raw = env_vars.get("MYSQL_PASSWORD", "")
        password = quote_plus(password_raw)
        host = env_vars.get("MYSQL_HOST", "localhost")
        port = env_vars.get("MYSQL_PORT", "3306")
        database = env_vars.get("MYSQL_DATABASE")

        if docker_mode and host == "localhost":
            host = "sql-db"

        connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)
        return engine

    except Exception as e:
        raise RuntimeError(f"Failed to create SQLAlchemy engine: {e}")


def test_connection(engine):
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return True
    except OperationalError as e:
        raise RuntimeError(f"❌ Could not connect to the database: {e}")


def get_schema_overview(engine):
    inspector = inspect(engine)
    schema = {}
    for table_name in inspector.get_table_names():
        columns = [col["name"] for col in inspector.get_columns(table_name)]
        schema[table_name] = columns
    return schema
