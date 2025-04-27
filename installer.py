try:
    import requests
except ImportError or ModuleNotFoundError:
    import subprocess
    subprocess.run(['pip','install','requests'])