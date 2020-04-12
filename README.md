# RMA
Implementation of selected Relational Matrix Algebra operations in MonetDB.

Go to the folder RMA_README and perform the following steps:

- Execute the commands in the file RMA_README.txt to install RMA+MonetDB.

- Run the command `./mclient -d demo < RMA_CreateData.sql` from the command 
line to create sample tables.

 - Run the command `./mclient -d demo --timer=performance < RMA_QueryData.sql` 
from the command line to perform sample queries. You can compare the output 
of mclient with output given in RMA_QueryDataOutput.txt.

- Perform the steps in file RMA_CreateTables.txt to repeat selected experiments.
