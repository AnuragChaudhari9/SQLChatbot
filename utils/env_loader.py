import os

def load_env_file(file):
    env_vars = {}

    for line in file:
        if isinstance(line, bytes):
            decoded = line.decode("utf-8").strip()
        else:
            decoded = line.strip()

        if decoded and not decoded.startswith("#") and "=" in decoded:
            key, value = decoded.split("=", 1)
            env_vars[key.strip()] = value.strip()

    return env_vars


