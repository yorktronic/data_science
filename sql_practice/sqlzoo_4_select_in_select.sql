###########################
# Section 4 - Select within Select Tutorial
# See the table and the questions here: http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial
###########################

# Question 1 - List each country name where the population is larger than 'Russia'
select name from world
	where population > 
		(select population from world where name = 'Russia')

# Question 2 - Show the countries in Europe with a per capita GDP greater than 'United Kingdom'	
select name from world 
	where ((gdp / population) >
		(select gdp / population from world where name = 'United Kingdom') and continent = 'Europe')

# Question 3 - List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
select name, continent from world
	where continent in (
		select continent from world where name in ('Argentina', 'Australia')
	)
	order by name

# Question 4 - Which country has a population that is more than Canada but less than Poland? Show the name and population
select name, population from world
	where (population > (select population from world where name = 'Canada')) 
	and (population < (select population from world where name = 'Poland'))

# Question 5 - Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany. Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.
select name, 
	CONCAT(ROUND((population / (select population from world where name = 'Germany') * 100), 0), '%')
	from world
	where continent = 'Europe'

# Question 6 - Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)
select name from world 
	where gdp > (select max(gdp) from world where continent = 'Europe')

# Or you can use the ALL function
select name from world
	where gdp > all (select gdp from world where continent = 'Europe' and gdp > 0)

