# How New Yorkers Bike #

I performed an analysis on how New Yorkers use the Citi Bike program in New York City on July 22, 2015. The data pull was run from 7:03 PM EST to 8:03 EST. This project was relatively straightforward, though I ran in to a few issues as I had never worked with Epoch time before. I performed this work in both Windows and in OSX, and after Windows being a pain in the a** cooperating with me going the system time route, I just finished the project on my Macbook Pro. 

I might make sure this works with Windows later on.

## So, what was the most active station during this timeframe? ##

The most active station was station id <a href="https://www.google.com/maps/place/40%C2%B043'34.4%22N+73%C2%B059'01.7%22W/@40.7613195,-73.9623898,12.5z/data=!4m2!3m1!1s0x0:0x0" target="_blank">432 at E 7 St & Avenue A. Latitude: 40.72621788 Longitude: -73.98379855</a>.

There were 77 bicycles coming and going in the hour between 2015-07-22 19:03:45 and 2015-07-22 20:03:13. Below is a graph showing the in and outs for all stations in NYC.

This seems to be accurate? I'll run the analysis again during a few more one-hour blocks to see what I come up with. For now, here's a plot of all the stations and their in and out values:

<figure>
	<img src="https://raw.githubusercontent.com/yorktronic/data_science/master/thinkful/Unit3/nyc-biking/plots/num-bikes-in-and-out-in-one-hour.png">
	<figcaption>The x-axis is just ID numbers of bike stations. There are 329 in total, not 3000 like you might think from looking at the graph.</figcaption>
</figure>

## How did I do it? ##

This was part of a tutorial through Thinkful's Data Science course, so I used some of their code that was part of the lesson. I broke the problem up using several scripts so that if I have to do something similar later, and any of this will be reusable, I'll... well, have it for later. The files:

**nyc-biking.py**: creates the SQLite database with the necessary tables
**getAvailableBikes.py**: pulls from the Citi Bikes JSON data and populates the database tables with the information I needed
**60-minutes.py**: runs getAvailableBikes.py once a minute for 60 minutes
**analysis.py**: performs the analysis, which I summarized above.

## Answers to other questions ##

1. Explore other data variables. Are there any test stations? **No.**
2. How may are not in service? **There are 329 total, and at the time I did this analysis there were 326 in service, so there were 3 not in service.**
3. Mean and median leaving the stations that aren't in service in the set: **12.7 and 11, respectively**
4. Mean and median leaving the stations that aren't in service out of the set: **12.8 and 11, respectively** (this makes sense since there are only 3 out of service stations)