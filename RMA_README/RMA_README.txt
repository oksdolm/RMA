This document describes how to download, compile, install and
start using our RMA+ extension of MonetDB system.

The extension of MonetDB is done on all levels of
the system, from parser to physical BAT operations. Consider the
extension of MonetDB with addition, QR decomposition, linear
regression, and copy to MKL format. In total it changes 20 files out
of approximately 4500 files (we excluded test and configuration
files) and includes additionally 2426 lines of code.

The main extensions are done in the following files:

sql/server/sql_parser.y
sql/server/rel_select.c
sql/server/rel_rel.c
sql/backends/monet5/rel_bin.c
sql/backends/monet5/sql_statement.c

Please refer to HowToStart.rst file in order to find official
installation guide from MonetDB. 

Prerequisites (Debian 4.9.210):
------------------------------

pkg-config:
apt install pkg-config

gcc:
apt install build-essentials

bison:
apt install bison

openssl:
apt install libssl-dev

gettext:
apt install gettext


Configure and Make
------------------

Perform bootstrap in the source directory:

./bootstrap

In the directory where folder with the source code (MonetDB-Mar2018) is located
create two directories BUILD and INSTALL:

mkdir BUILD
mkdir INSTALL


Configure
~~~~~~~~~

Then in BUILD directory give the following command to reach maximal optimisation:

../MonetDB-Mar2018/configure --prefix=/root_to_INSTALL_folder/INSTALL/ --disable-debug --disable-assert --enable-optimize

The directory where you execute ``configure`` is the place where all
intermediate source and object files are generated during compilation
via ``make``.  It is useful to have this be a new directory so that
there is an easy way to remove all intermediates in case you want to
rebuild (just empty or remove the directory).

Please notice that --prefix must include absolute path.


Make and Install
~~~~~~~~~~~~~~~~

In the same directory BUILD (where you called ``configure``) give the
command:


make && make install


By default (if no ``--prefix`` option was given to ``configure`` above),
this will install in ``/usr/local``.  Make sure you have appropriate
privileges.


Usage
-----

Examples of Queries
~~~~~~~~~~~~~~~~~~~

The important binary files are installed in INSTALL/bin directory.

To run MonetDB server interactively:

1) run the server:
./INSTALL/bin/mserver5

2) run the client:
./INSTALL/bin/mclient 
(user: monetdb, password: monetdb)

In order to show the execution time add --timer=performance flag to ./mclient

This connects you to the demo database.

To quit type \q in both processes.

If you want to execute sample files (RMA_CreateData.sql and RMA_QueryData.sql) 
run mclient as follows:

./mclient -d demo --timer=performance  < /path_to_RMA_CreateData.sql/RMA_CreateData.sql
./mclient -d demo --timer=performance  < /path_to_RMA_QueryData.sql/RMA_QueryData.sql

In case the result of an operation is too big and you want to discard it add -f trash flag to mclient.


Repeating Selected Experiments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to file RMA_CreateTables.txt to repeat selected experiments.
