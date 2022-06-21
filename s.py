from PIL import Image, ImageTk
from dtr_time import *

current_time = timeNow()# GETTING TIME RIGHT NOW FROM DTR_TIME.PY
date = dateNow()# GETTING DATE TODAY FROM DTR_TIME.PY

# T MEANS THE TIME BASIS OF CONSIDERATION AS LATE
t = datetime.time(11, 11, 00) # FORMAT ( HOUR/S, MINUTE/S, SECONDS )
t1 = t.strftime("%H:%M:%S") # FIXNG THE TIME FORMAT

# IF YOU ARE NOT LATE
if(t1 > current_time):
    status = ""
# YOURE PRETTY LATE
elif(t1 <= current_time):
    status = "Late"

print(current_time)
print(status)

