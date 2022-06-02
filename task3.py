import os
import platform

pid = os.getpid()
username = os.getlogin()
system = platform.system()
release = platform.release()


print(f"This script has the following PID: {pid}. It was ran by {username} to work happily on {system}-{release}")