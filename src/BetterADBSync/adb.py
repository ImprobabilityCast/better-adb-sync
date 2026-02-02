import os


def find_adb_executable():
    adb_env = os.environ.get("ADB")
    if adb_env is not None and os.path.isfile(adb_env) and os.access(adb_env, os.X_OK):
        return adb_env

    if os.name == 'nt':
        adb_executable = 'adb.exe'
    else:
        adb_executable = 'adb'

    android_home_env = os.environ.get("ANDROID_HOME")
    if android_home_env is not None:
        android_home_env = os.path.join(android_home_env, "platform-tools", adb_executable)
        if os.path.isfile(android_home_env) and os.access(android_home_env, os.X_OK):
            return android_home_env

    path_env = os.environ.get("PATH", "").split(os.pathsep)

    for path in path_env:
        path = path.strip('"')  # handle quoted PATH entries
        candidate = os.path.join(path, adb_executable)
        print(candidate)
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    raise FileNotFoundError(f"Could not find {adb_executable}")
