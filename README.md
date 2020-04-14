# RMA
RMA is the extension of SQL and column store MonetDB with matrix operations defined over relations, 
that preserve contextual information.
Detailed information is given in the paper `"A relational matrix algebra and its implementation in a column store"`,  SIGMOD 2020, and in our technical report http://arxiv.org/abs/2004.05517.

This repositoty includes the implementation of selected Relational Matrix Algebra operations in MonetDB.

Go to the folder RMA_README and perform the following steps:

- Execute the commands in the file RMA_README.txt to install RMA+MonetDB.

- Run the command `./mclient -d demo < RMA_CreateData.sql` from the command 
line to create sample tables.

 - Run the command `./mclient -d demo --timer=performance < RMA_QueryData.sql` 
from the command line to perform sample queries. You can compare the output 
of mclient with output given in RMA_QueryDataOutput.txt.

- Perform the steps in file RMA_CreateTables.txt to repeat selected experiments.

Example queries:





