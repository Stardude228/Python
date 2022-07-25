# Slash commands
* '\c' - to which database we are connected and through which user
* '\c name_of_db' - switching over to this database
* '\l' - shows all databases
* '\dt' - shows all tables in database that we are connected to
* '\du' - shows all users
* '\q' - quite database

# Creation of database and tables
```sql
CREATE DATABASE name_of_db;
-- creates database
-- (-- comment in sql)

CREATE TABLE name_of_table (
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ...
);
-- creates tables with fields
```

# Filling the tables
```sql
INSERT INTO name_of_table (name_of_column1, name_of_column2)
VALUES (value1, value2), (value11, value22);
-- adds a record into the table
``` 

# Output of data from table
```sql
SELECT * FROM name_of_table;
-- Displays every field from the table
```

```sql
SELECT name_of_column1, name_of_column1 FROM name_of_table;
-- Displays mentioned fields from the table
```

```sql
SELECT * FROM name_of_table WHERE name_of_column2 = 'hello';
-- Displays every field from the table that has the value hello in name_of_column2 column
```

# Connection
## pk fk
> primary key (pk) - main internal key
> it is a constraint that we specify in those fields that has to be unique in order to use them later in connections

> foreign key (fk) - external key
> it is a constraint that we specify in those fields that have pk for creation of connections

```sql
CREATE TABLE flag (
    id serial primary key,
    first_name varchar(60),
    last_name varchar(60)
);
CREATE TABLE book (
    id serial,
    title varchar(50),
    published year,
    author_id int,
    constraint fk_author_book
    Foreign key (author_id)
    references author (id)
)
```

## Types of connections (theory)
> One to one
* One country - one flag
* One person - one heart

> One to many
* One Oomat - many congratulations 
* One country - many cities

> Many to many
* Mentor have many students - Student has many mentors
* Social network have many users - User has many social networks

### One to one (practice)
```sql
CREATE TABLE flag (
    id serial primary key,
    photo text
);
CREATE TABLE country (
    id serial primary key,
    title varchar(50),
    flag_id int unique,
    CONSTRAINT fk_country_flag
    Foreign key (flag_id)
    references flag (id)
);
```


### One to many (practice)
```sql
CREATE TABLE post (
    id serial primary key,
    title varchar(100),
    body text
);
CREATE TABLE comment (
    id serial primary key,
    body text,
    created_at datetime,
    post_id int,
    CONSTRAINT fk_post_comment
    Foreign key (post_id)
    references post (id)
);
```


### Many to many (practice)
```sql
CREATE TABLE student (
    id serial primary key,
    first_name varchar(50),
    age int
);
CREATE TABLE mentor (
    id serial primary key,
    first_name varchar(50),
    age int
);
CREATE TABLE student_mentor (
    student_id int,
    mentor_id int,

    CONSTRAINT fk_student
    Foreign key (student_id)
    references student (id),

    CONSTRAINT fk_mentor
    Foreign key (mentor_id)
    references mentor (id)
);
```

## JOIN (theory)
> JOIN - instruction that allows in SELECT requests take data from several connected tables

> INNER JOIN (JOIN) - when recodrs with full connections are being pulled out

> FULL JOIN - when all recodrs are being pulled out (disregarding the fact that they may not have full connections)

> LEFT JOIN - when recodrs of the left side and records with full connections are being pulled out
> RIGHT JOIN - when recodrs of the right side and records with full connections are being pulled out

## join (practice)

### one to one
```sql
SELECT country.title, flag.photo
FROM country
JOIN flag
ON country.flag_id = flag.id;
```

### one to many
```sql
SELECT post.title, comment.body, comment.created_at
FROM post
JOIN comment
ON post.id = comment.post_id;
```

### many to many
```sql
SELECT mentor.first_name as mentor_name, student.first_name as student_name
FROM mentor

JOIN student_mentor
ON mentor.id = studen_mentor.mentor_id


JOIN student
ON student.id = studen_mentor.student_id;
```

# Import / Export data
write from file to db
```bash
psql db_name < file.sql
```
write from db to file
```bash
pg_dump db_name > file.sql
```