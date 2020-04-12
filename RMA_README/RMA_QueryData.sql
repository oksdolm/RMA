--This file includes the quiries of sample tables 
--Currently add, qqr, sol, cpd, and lapack are supported
--Please notice that in this version ordering is switched off
--Please notice that now only type double is supported in attributes included in application schema
--Currently in implementation you still must specify application schema explicitly 
--Currently joins and selections does not work right after matrix operations, when they involve a new relation. Please create table and then apply them

select * 
from qqr (t1 on x2, x3 order by x1);

select * 
from qqr (t1 on x2 order by x1);

select * 
from qqr (t2 on y4 order by y1, y2);

select * 
from (t1 on x2, x3 order by x1) add (t2 on y3, y4 order by y1);

select * 
from qqr (t2 on y4, y3 order by y1, y2);

select * 
from qqr ((select * 
    from  t1 join t2 on x1 = y2 ) t on y3, x2, x3 order by x1, x2);

with t as (select * 
    from qqr (t2 on y4, y3 order by y1, y2)) 
select * 
from t ;

select * 
from (select * 
    from (t2 on y4, y3 order by y1, y2) cpd (t2 on y4, y3 order by y1, y2)) t 
    join t2 on t.y4 > t2.y3;

select * 
from (select * 
    from (t2 on y4, y3 order by y1, y2) cpd (t1 on x2, x3 order by x1)) t 
    join t2 on t.x3 > t2.y3;

select t2.y1, t2.y2, x2, x3, y3, y4  
from (select * 
    from (t2 on y4, y3 order by y1, y2) cpd (t1 on x2, x3 order by x1)) t 
    join t2 on t.x3 > t2.y3;

select * 
from qqr( (select t2.y1, t2.y2, x2, x3, y3, y4  from (select * from (t2 on y4, y3 order by y1, y2) cpd (t1 on x2, x3 order by x1)) t 
        join t2 on t.x3 > t2.y3) ttt  
    on ttt.x2, ttt.y3, ttt.y4 order by ttt.y1, ttt.x3 );

select * 
from qqr((select * 
        from (t2 on y4, y3 order by y1, y2) cpd (t1 on x2, x3 order by x1))  t 
    on x2, x3 order by y1);

select * 
from qqr ((select * from t1 where x2 > 1) t on x2, x3 order by x1);

select y3, y4 
from (select * from (t2 on y4, y3 order by y1, y2) cpd (t2 on y4, y3 order by y1, y2)) t;

select * 
from qqr ((select * from t1 join t2 on t1.x1 = t2.y2) t on x2, x3 order by x1);

select * 
from qqr ((select * from t1 where x2 > 4) t on x2, x3 order by x1);



