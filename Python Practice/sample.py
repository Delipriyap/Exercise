
import os


file=os.system("gnome-terminal -e  'bash -c \"ifconfig; exec bash \"'")
print(file)
