# Relational Matrix Algebra
## For research paper SIGMOD 2020 
Relational Matrix ALgebra (RMA) is the extension of SQL and column store MonetDB with matrix operations defined over relations 
that preserve contextual information.


Detailed information is given in the paper 

`O. Dolmatova, N. Augsten, and M. H. Böhlen. A relational matrix 
algebra and its implementation in a column store. In Proceedings of the 2020 ACM SIGMOD International Conference on Management of Data. SIGMOD'20, June 14-19, 2020, Portland, OR, USA, 2020. ACM.` 

and in our technical report http://arxiv.org/abs/2004.05517.

This repository includes the implementation of selected Relational Matrix Algebra operations in MonetDB.

#### Installation and usage:

Go to the folder RMA_README and perform the following steps:

- Execute the commands in the file RMA_README.txt to install RMA+MonetDB.

- Run the command `./mclient -d demo < RMA_CreateData.sql` from the command 
line to create sample tables.

 - Run the command `./mclient -d demo --timer=performance < RMA_QueryData.sql` 
from the command line to perform sample queries. You can compare the output 
of mclient with output given in RMA_QueryDataOutput.txt.

- Perform the steps in file RMA_CreateTables.txt to repeat selected experiments.

#### Example queries:

`CREATE TABLE t1 (x1 STRING, x2 DOUBLE, x3 DOUBLE);`

`CREATE TABLE t2 (y1 STRING, y2 STRING, y3 DOUBLE, y4 DOUBLE);`

Consider the following query:

`SELECT * FROM qqr (t1 ON x2, x3  BY x1);`

and input relation:

t1                          

| x1   | x2      | x3      |
|------|---------|---------|
| ann  |       0 |       7 |
| joe  |       9 |       4 |
| pit  |       6 |       5 |
| ken  |       7 |       2 |
| lea  |       3 |       1 |
| bob  |       1 |       0 |

Attribute x1 in t1 is used to determine the order of tuples for matrix calculation: 

ordered t1

| x1   | x2      | x3      |
|------|---------|---------|
| ann  |       0 |       7 |
| bob  |       1 |       0 |
| joe  |       9 |       4 |
| ken  |       7 |       2 |
| lea  |       3 |       1 |
| pit  |       6 |       5 |

The ordered values of x1 and x3 are interpreted as an input matrix for the QQR decomposition (returns only matrix Q).
The query returns relation qqr(t1), where attribute x1 can be used again to determine the order for the further computations.

qqr(t1)
| x1   | x2                       | x3                       |
|------|--------------------------|--------------------------|
| ann  |                        0 |       0.9366029597764617 |
| bob  |      0.07537783614444091 |     -0.06309906303688825 |
| joe  |       0.6784005252999682 |     -0.03268987603115907 |
| ken  |       0.5276448530110863 |      -0.1740925956078001 |
| lea  |      0.22613350843332272 |     -0.05549676628545596 |
| pit  |      0.45226701686664544 |       0.2904077359047145 |



The examples below follow the same structure.

The following query returns relation Q from QR decompisition applied to values in attributes x2 and x3 in relation t (subset of relation t1) ordered by attribute x1:

`SELECT * FROM qqr ((SELECT * FROM t1 WHERE x2 > 1) t ON x2, x3  BY x1);`

The following query performs addition between attributes x2, x3 and y3, y4 from relations t1 and t2 ordered by x1 and y1, respectively:

`SELECT * FROM (t1 ON x2, x3  BY x1) add (t2 ON y3, y4  BY y1);`

More examples are given in the file RMA_README/RMA_QueryData.sql.



