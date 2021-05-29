
* **本文件提供关于cs50的sql一讲中课后习题的解答，仅作为参考，如存在错误请指出。**

* cs50 sql一讲的习题总共分为两个部分：（链接中有详细的题目说明与所需文件）
* 1、关于sql语言的运用，熟悉sql语法的运用，题目链接：https://cs50.harvard.edu/summer/2020/psets/7/movies/ 
* 2、关于使用python链接数据库进行一些简单的操作，题目链接：https://cs50.harvard.edu/summer/2020/psets/7/houses/
* 第一题共13小问，每一小问的要求是根据相应的查询需求写出对应sql语句，所使用的为movies.db文件。答案放在下方：
```
1、select title from movies 
where movies.year = 2008;

2、select birth from people 
where name = 'Emma Stone';

3、select title from movies 
where year >= 2018 order by title;

4、select count(*) from ratings where rating = 10.0;
 select count(title) from movies where id in (select movie_id from ratings where rating = 10.0);

SELECT COUNT(title) FROM movies
JOIN ratings on movies.id = ratings.movie_id
WHERE rating = 10;

5、select title,year from movies 
where title like "Harry Potter%" order by year;

6、select avg(rating) from ratings where movie_id in (select id from movies where movies.year = 2012);
select avg(rating) from ratings INNER JOIN movies ON ratings.movie_id = movies.id where movies.year = 2012;

7、select title,rating from movies inner join ratings on movies.id = ratings.movie_id where year = 2010 order by rating DESC,title;

8、  
select name from stars 
INNER JOIN people ON stars.person_id = people.id
INNER JOIN movies ON stars.movie_id = movies.id
where movies.title = 'Toy Story';
  
SELECT name from people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title = "Toy Story";


9、select DISTINCT(name) from stars 
INNER JOIN people ON stars.person_id = people.id
INNER JOIN movies ON stars.movie_id = movies.id
where movies.year = 2004 order by people.birth;

10、select name from people 
INNER JOIN directors ON people.id = directors.person_id 
INNER JOIN movies ON directors.movie_id = movies.id 
INNER JOIN ratings ON movies.id = ratings.movie_id 
where rating >= 9;

11、select title from people 
INNER JOIN stars ON people.id = stars.person_id 
INNER JOIN movies ON stars.movie_id = movies.id 
INNER JOIN ratings ON movies.id = ratings.movie_id 
where people.name = 'Chadwick Boseman' order by rating DESC limit 5;

12、
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Johnny Depp"
INTERSECT
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter";

13、select DISTINCT(name) from people 
INNER JOIN stars ON people.id = stars.person_id 
INNER JOIN movies ON stars.movie_id = movies.id 
where title in (SELECT title from people 
	JOIN stars ON people.id = stars.person_id 
	JOIN movies ON stars.movie_id = movies.id 
	WHERE name = 'Kevin Bacon' and birth = 1958) AND (people.name != 'Kevin Bacon');
```
* 第二题是关于使用python调用数据库的，其中两个小问，第一个小问是将characters.csv文件中的数据读入到studens.db中去，代码放在import.py中，第二个小问是将students.db中的数据按照一定的查询要求和格式读出来，代码放在roster.py中。

