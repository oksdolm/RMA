--This file includes the creation of sample tables 
--Currently add, qqr, sol, cpd, and lapack are supported
--Please notice that in this version ordering is switched off
--Please notice that now only type double is supported in attributes included in application schema
--Currently in implementation you still must specify application schema explicitly 
--Currently joins and selections does not work right after matrix operations, when they involve a new relation. Please create table and then apply them

create table t1 (x1 string, x2 double, x3 double);
insert into t1 values ('ann', 0, 7);
insert into t1 values ('joe', 9, 4);
insert into t1 values ('pit', 6, 5);
insert into t1 values ('ken', 7, 2);
insert into t1 values ('lea', 3, 1);
insert into t1 values ('bob', 1, 0);


create table t2 (y1 string, y2 string, y3 double, y4 double);
insert into t2 values ('CA','ann', 13, 43);
insert into t2 values ('NY','bob', 24, 5);
insert into t2 values ('IL','cue', 87, 0);
insert into t2 values ('KL','ola', 98, 76);
insert into t2 values ('HW','lea', 34, 32);
insert into t2 values ('AK','sam', 21, 37);

