start transaction;
create table t3220 (y double, z real);
insert into t3220 values (0,0);
insert into t3220 values (0.1,0.1);
insert into t3220 values (-0.1,-0.1);
insert into t3220 values (-0.2,-0.2);
insert into t3220 values (0.2,0.2);
select * from t3220;
select * from t3220 where y = 0;
select * from t3220 where z = 0;
select * from t3220 where y < 0;
select * from t3220 where z < 0;
select * from t3220 where y > 0;
select * from t3220 where z > 0;
select * from t3220 where y <> 0;
select * from t3220 where z <> 0;
select * from t3220 where y > 0.1;
select * from t3220 where y < 0.1;
select * from t3220 where y < -0.1;
select * from t3220 where y > -0.1;
rollback;
