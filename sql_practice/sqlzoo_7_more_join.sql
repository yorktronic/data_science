###########################
# Section 7 - More JOIN
# See the table and the questions here: http://sqlzoo.net/wiki/More_JOIN_operations
###########################

# Question 1 - List the films where the yr is 1962 [Show id, title]
select id, title from movie
	where yr = 1962

# Question 2 - Give year of 'Citizen Kane'
select yr from movie
	where title = 'Citizen Kane'

# Question 3 - List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
select id, title, yr from movie
	where title like 'Star Trek%'
	order by yr

# Question 4 - What are the titles of the films with id 11768, 11955, 21191?
select title from movie
	where id in (11768, 11955, 21191)

# Question 5 - What title does the acress 'Glenn Close' have?
select id from actor
	where name = 'Glenn Close'

# Question 6 - What is the id of the film 'Casablanca'?
select id from movie
	where title = 'Casablanca'

# Question 7 - Obtain the cast of 'Casablanca'
select name from actor join casting on (id = actorid)
	where movieid = 11768

# Question 8 - Obtain the cast list for the film 'Alien'
select name 
	from actor join casting on (id = actorid)
	where movieid = (select id from movie where title = 'Alien')

# Question 9 - List the films in which Harrison Ford has appeared
# Get the actor id from actor using his name, get the movie ID's from casting for all movies he's been in, then get the titles of all the movies using the movie IDs 
select title from movie
	where id in 
		(select movieid
		from actor join casting on (id = actorid)
		where name = 'Harrison Ford')
order by yr #ordered by year because I was wondering what his first movie was

# Question 10 - List the films where 'Harrison Ford' has appeared - but not in the starring role. [Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]
select title from movie
	where id in 
		(select movieid
		from actor join casting on (id = actorid)
		where (name = 'Harrison Ford' and ord != 1))
order by yr

# Question 11 - List the films together with the leading star for all 1962 films
# Get all the movie ids for 1962 from the movie table
# Get all the actorids for those movieids from the casting table
# Get the names of those actors from the actor table
select movie.title, actor.name
	from movie join casting on (movie.id = casting.movieid)
	join actor on (casting.actorid = actor.id)
	where (movie.yr = 1962 and casting.ord = 1)

# Question 12 - Which were the busiest years for John Travolta? Show the year and the number of movies he made for any year when he made more than two movies
# Get his actorid from the actor table
# Get a list of movie ids from the casting table
# Group the movies by date and count the number of them using the movie table
select movie.yr, count(movie.id)
	from movie
	where id in (
		select movieid from casting
		where actorid = (select id from actor where name = 'John Travolta')
	)
group by movie.yr having count(movie.id) > 2




