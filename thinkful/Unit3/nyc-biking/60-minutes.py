####################################
#
# Calls update-available-bikes.py every minute for 60 minutes to create one hour's worth of available bikes data in ./db/citi_bike.db
#
####################################

# Import the time library so I can create a time delay
import time

t = 0
while t < 60:
	execfile("./getAvailableBikes.py")
	t += 1
	time.sleep(60)