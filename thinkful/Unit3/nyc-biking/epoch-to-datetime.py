# Messing around with epoch and datetime to figure out exactly how epoch time works.

import datetime

epoch = 1437617025
dt = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

print dt