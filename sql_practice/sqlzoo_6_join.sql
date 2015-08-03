###########################
# Section 6 - Join
# See the table and the questions here: http://sqlzoo.net/wiki/The_JOIN_operation
###########################

# Question 1 - Show matchid and player name for all goals scored by Germany. teamid = 'GER'
select matchid, player from goal
	where teamid = 'GER'

# Question 2 - Show id, stadium, team1, team2 for game 1012
select id, stadium, team1, team2 from game
	where id = 1012

# Question 3 - Show the player, teamid, and mdate for every German goal
select player, teamid, mdate
	from game join goal on (id = matchid)
	where teamid = 'GER'

# Question 4 - Show the team1, team2 and player for every goal scored by a player called Mario
select team1, team2, player
	from game join goal on (id = matchid)
	where player like 'Mario%'

# Question 5 - Show player, teamid, coach, gtime for all goals scored in the first 10 minutes
select player, teamid, coach, gtime
	from goal join eteam on (teamid = id)
	where gtime < 10

# Question 6 - List the the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.
select mdate, teamname
	from game join eteam on (team1 = eteam.id)
	where coach = 'Fernando Santos'

# Question 7 - List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'
select distinct player
	from game join goal on (id = matchid)
	where stadium = 'National Stadium, Warsaw'

# Question 8 - show the name of all players who scored a goal against Germany in the Germany-Greece quarterfinal game
select distinct player
	from game join goal on (id = matchid)
	where (team2 = 'GER' or team1 = 'GER') and teamid != 'GER'

# Question 9 - Show teamname and the total number of goals scored
select teamname, count(teamid)
	from goal join eteam on (teamid = id)
	group by teamname

# Question 10 - Show the stadium and the number of goals scored in each stadium
select stadium, count(matchid)
	from game join goal on (id = matchid)
	group by stadium

# Question 11 - For every match involving 'POL', show the matchid, date and the number of goals scored.
select matchid, mdate, count(matchid)
	from game join goal on (id = matchid)
	where (team1 = 'POL' or team2 = 'POL')
	group by matchid

# Question 12 - For every match where 'GER' scored, show matchid, match date, and the number of goals scored by 'GER'
select matchid, mdate, count(teamid)
	from game join goal on (id = matchid)
	where (team1 = 'GER' or team2 = 'GER') and teamid = 'GER'
	group by matchid

# Question 13 - List every match with the goals scored by each team as shown
select mdate, team1, 
	sum(case when teamid = team1 then 1 else 0 end) as score1, 
	team2, 
	sum(case when teamid = team2 then 1 else 0 end) as score2

	from game left join goal on (id = matchid)
	group by id
	order by mdate, matchid, team1, team2
