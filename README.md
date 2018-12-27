Log-Analysis:

About:
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.

Building an informative summary from logs is a real task that comes up very often in software engineering.The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.


Pre-Requisites:
Python3
Vagrant
VirtualBox


Project Setup:
1. Install Vagrant and VirtualBox
  1.Download or Clone fullstack-nanodegree-vm repository.
  2.Download the data from Udacity website.
  3.Unzip this file after downloading it. The file inside is called newsdata.sql.
  4.Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from Here
2. Launching the Virtual Machine:
  1.Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
  2.Then Log into this using command:
  $ vagrant ssh
  3.Change directory to /vagrant and look around with ls.
3. Setting up the database and Creating Views:
  1.Load the data in local database using the command:
  psql -d news -f newsdata.sql
  2.The database includes three tables:

  The authors table includes information about the authors of articles.
  The articles table includes the articles themselves.
  The log table includes one entry for each time a user has accessed the site.
  
  Use psql -d news to connect to database.

Create view article_view using:

  ```create view article_view as select title,author,count(*) as views from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author
  order by views desc;```


Create vier error_log_view using:

  ```create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
  then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
  order by "Percent Error" desc;```


Running the queries:
From the vagrant directory inside the virtual machine,run logs.py using:
  $ python3 project1.py