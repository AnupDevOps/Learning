# Python MySQL

# Python can be used in database applications.
# One of the most popular database is MySQL

# Install MySQL Driver
# Python needs a MySQL driver to access the MySQL database.
# In this tutorial we will use the driver "MySQL Connector".
# We recommend that you use PIP to install "MySQL Connector".
# PIP is most likely already installed in your Python environment.
# Navigate your command line to the location of PIP, and type the following.

# download and install Mysql Connector
# python -m pip mysql-connector

# Test MySQL Connector
# To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content.

import mysql.connector

# If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.

# Create Connection
# Start by creating a connection to the database.
# Use the username and password from your MySQL database.

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="admin",
	auth_plugin='mysql_native_password'
	)
	
print(mydb)