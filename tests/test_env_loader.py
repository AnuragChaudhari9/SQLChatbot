# tests/test_env_loader.py

from utils.env_loader import load_env_file
from io import StringIO

def test_load_env_file_reads_variables_correctly():
    fake_env_content = b"DB_HOST=localhost\nDB_USER=root\nDB_PASSWORD=1234\n"
    fake_file = StringIO(fake_env_content.decode())

    env_dict = load_env_file(fake_file)

    assert env_dict["DB_HOST"] == "localhost"
    assert env_dict["DB_USER"] == "root"
    assert env_dict["DB_PASSWORD"] == "1234"
