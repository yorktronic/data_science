###########################
# Section 3 - Select from Nobel
# See the table and the questions here: http://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial
########################### 

# Question 1 - Display nobel prizes for 1950
select yr, subject, winner from nobel
	where yr = 1950

# Question 2 - Show who won the 1962 prize for Literature
select winner from nobel
	where yr = 1962 and subject = 'Literature'

# Question 3 - Show the year and subject that won 'Albert Einstein' his prize
select yr, subject from nobel
	where winner = 'Albert Einstein'

# Question 4 - Give the name of the 'Peace' winners since the year 2000, including 2000
select winner from nobel
	where subject like 'Peace%' and yr >= 2000

# Question 5 - Shwo all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive
select yr, subject, winner from nobel
	where yr between 1980 and 1989 and subject = 'Literature'

# Question 6 - Show the details of the presidential winners Theodore Roosevelt, Woodrow Wilson, Jimmy Carter
select * from nobel
	where winner in ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter')
	