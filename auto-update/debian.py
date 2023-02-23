import subprocess
import datetime

now = datetime.datetime.now()
LOG_FILE = f"/var/log/system-updates-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.log"

# open log file
log_file = open(LOG_FILE, "a")

# Update package lists
log_file.write(f"Updating package lists at {now}\n")
subprocess.run(["apt-get", "update"])

# Upgrade all packages
log_file.write(f"Upgrading all packages at {datetime.datetime.now()}\n")
subprocess.run(["apt-get", "-y", "upgrade"])

# close log file
log_file.close()
