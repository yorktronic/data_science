###########################
# Section 5 - Sum and Count
# See the table and the questions here: http://sqlzoo.net/wiki/SUM_and_COUNT
########################### 

# Question 1 - Show the total population of the world.
select sum(population) from world

# Question 2 - List all the continents - just one each
select distinct continent from world

# Question 3 - What is the total GDP of Africa?
select sum(gdp) from world 
	where continent = 'Africa'

# Question 4 - How many countries have an area of at least 1000000
select count(distinct name) from world
	where area >= 1000000

# Question 5 - What is the total population of France, Germany and Spain?
select sum(population) from world
	where name in ('France', 'Germany', 'Spain')

# Question 6 - For each continent show the continent and number of countries
select continent, count(name) from world
	group by continent

# Question 7 - For each continent show the continent and number of countries with a population of at least 10M
select continent, count(name) from world
	where population > 10000000
group by continent

# Question 8 - List the continents that have a total population of at least 100 million
select continent from world
group by continent
having sum(population) >= 100000000