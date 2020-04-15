# Relational Matrix Algebra
## For research paper SIGMOD 2020 
Relational Matrix ALgebra (RMA) is the extension of SQL and column store MonetDB with matrix operations defined over relations 
that preserve contextual information.
Detailed information is given in the paper `"A relational matrix algebra and its implementation in a column store"`,  SIGMOD 2020, and in our technical report http://arxiv.org/abs/2004.05517.

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

Consider two relations with the following create statements:

`CREATE TABLE t1 (x1 STRING, x2 DOUBLE, x3 DOUBLE);`

`CREATE TABLE t2 (y1 STRING, y2 STRING, y3 DOUBLE, y4 DOUBLE);`

The following query returns relation Q from QR decompisition applied to values in attributes x2 and x3 in relation t1 ordered by attribute x1:

`SELECT * FROM qqr (t1 ON x2, x3  BY x1);`

The following query returns relation Q from QR decompisition applied to values in attributes x2 and x3 in relation t (subset of relation t1) ordered by attribute x1:

`SELECT * FROM qqr ((SELECT * FROM t1 WHERE x2 > 1) t ON x2, x3  BY x1);`


The following query performs addition between attributes x2, x3 and y3, y4 from relations t1 and t2 ordered by x1 and y1, respectively:

`SELECT * FROM (t1 ON x2, x3  BY x1) add (t2 ON y3, y4  BY y1);`





