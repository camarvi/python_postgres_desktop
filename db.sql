
CONECTARSE POR CONSOLA :

psql -h localhost -p 5432 -U postgres tareas 


SENTENCIAS

CREATE TABLE students(id serial, name text, address text, age int, PRIMARY KEY (id));

INSERT INTO students(name, address, age) values ('ryan', 'albacete' , 36);

INSERT INTO students(name, address, age) values ('mary', 'salamanca' ,  26);

select * from students;