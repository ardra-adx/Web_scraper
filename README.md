# Web_scraper

#scrape 
python script automatically collect job postings from job website like linkedln or indeed

#html-> beautifulSoup
#flask-
to create a web dashboard display also sxrape the job data and is user friendly

#install requierments text
flask
requests
beautifulSoup

#here used RemoteOK for jobs
 using scraper function they make a request to a specific job listing webpage
 parse the html
 extarct the job titles,companies and locations
 return the list of dictionaries each representing a job

 #URL setup
 request headers - user agent is set to stimulate a real browser
 
#parse the html with beautifulSoup
response text-contains the raw html code of the web page
beautiful Soup- parse the html and allows to navigate &search through it easily

#loop through each job entry on the page
all <tr> [table row] elements that have the class job
each <tr> represents job listing in the page 

#extract the job details
title 
company
location 

#save valid job entites 
strip() to remove whitespace 
check whether title & company exists

render template-> render html templates in this dashboard.html

@app.route-> maps the url path to the home()function


![Screenshot from 2025-05-28 20-54-01](https://github.com/user-attachments/assets/39a76e47-72a3-423e-9a3d-97d9e9c05204)




