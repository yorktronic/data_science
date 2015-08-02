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

# Question 7 - Show the winners with the first name John
select winner from nobel
	where winner like 'John%'

# Question 8 - Show the Physics winners for 1980 with the Chemistry winners for 1984
select winner from nobel
	where (subject = 'Physics' and yr = 1980) or (subject = 'Chemistry' and yr = 1984)

# Question 9 - Show the winners for 1980 excluding Chemistry and Medicine
select yr, subject, winner from nobel
	where (yr = 1980) and subject not in ('Medicine', 'Chemistry')

# Qeustion 10 - Show who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)
select yr, subject, winner from nobel
	where (yr < 1910 and subject = 'Medicine') or (yr >= 2004 and subject = 'Literature')

# Question 11 - Find all the details of the prize winner Peter Grünberg
select * from nobel
	where winner = 'Peter Grünberg'

# Question 12 - Find all the details of the prize won by Eugene O'Neill
select * from nobel
	where winner = "Eugene O'Neill"

# Question 13 - List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order
select winner, yr, subject from nobel
	where winner like 'Sir%'
	order by yr desc, winner asc

# Question 14 - The expression subject IN ('Chemistry','Physics') can be used as a value - it will be 0 or 1. Show the 1984 winners ordered by subject and winner name; but list Chemistry and Physics last.
select winner, subject, subject in ('Chemistry', 'Physics') from nobel
	where yr = 1984
	order by subject in ('Chemistry', 'Physics') asc, subject, winner



