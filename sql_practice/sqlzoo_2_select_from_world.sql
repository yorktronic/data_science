###########################
# Section 2 - Select from world
# See the table and the questions here: http://sqlzoo.net/wiki/SQLZOO:SELECT_from_WORLD_Tutorial
########################### 

# Question 2 - Show the name of the countries that have a population of at least two million
select name from world
where population >= 200000000

# Question 3 - Give the name and the per capita GDP for those countries with a population of at least two million
select name, gdp / population from world
where population >= 200000000

# Question 4 - Show the name and population in millions for the countries of the continent 'South America'
select name, population / 1000000 from world
where continent = 'South America'

# Question 5 - Show the name and population of France, Germany, and Italy
select name, population from world
where name in ('France', 'Germany', 'Italy')

# Question 6 - Show the countries which have a name that includes the word 'United'
select name from world
where name like 'United%'

# Question 7 - Show the countries that are big by area or big by population. Show name, popupulation, and area
select name, population, area from world
where population > 250000000 or area > 3000000

# Question 8 - Exclude countries that are big in both area and population
select name, population, area from world
where population > 250000000 xor area > 3000000

# Question 9 - Show the name and population in millions and the GDP in billions for the countries of the continent 'South America'
select name, round(population / 1000000, 2), round(gdp / 1000000000, 2) from world
where continent = 'South America'

# Question 10 - Show the per-capita GDP for those countries with a GDP of at least one trillion. Round this to the nearest 1000
select name, round(gdp / population, -3) from world
where gdp > 1000000000000

# Question 11 - Show the name and the continent - but substitute Australasia for Oceania - for countries beginning with N
select name,
	case when
	continent = 'Oceania' then 'Australasia'
	else continent
	end
from world where name like 'N%'

# Question 12 - Show the name and the continent - but substitute Eurasia for Europe and Asia; substitute America - for each country in North America or South America or Caribbean. Show countries beginning with A or B
select name, 
	case 
		when continent in ('Europe', 'Asia') then 'Eurasia'
		when continent in ('North America', 'South America', 'Caribbean') then 'America'
		else continent
	end
from world where name like 'A%' or name like 'B%'

# Question 13 - Oceania becomes Australasia, Countries in Eurasia and Turkey go to Europe/Asia, Carribean islands starting with 'B' go to North America, other Caribbean islands go to South America
select name, continent, 
	case
		when continent = 'Oceania' then 'Australasia'
		when continent = 'Eurasia' then 'Europe/Asia'
		when name = 'Turkey' then 'Europe/Asia'
		when continent = 'Caribbean' and name like 'B%' then 'North America'
		when continent = 'Caribbean' and name not like 'B%' then 'South America'
		else continent
	end
from world 
order by name 
# The order by statement is only necessary because a bug in SQLZoo's site














