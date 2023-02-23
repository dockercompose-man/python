import subprocess
import datetime

now = datetime.datetime.now()
LOG_FILE = f"/var/log/system-updates-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.log"

# open log file
log_file = open(LOG_FILE, "a")
