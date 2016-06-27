# A web crawler to track the trend of technologies(WIP)

If you are wondering what technologies that companies use nowsdays, you probably will just google it 
```
"Tell me the hottest techs used recently"
```
and you will probably get hundreds of thousands of results. Also, you could just go on a website like [techstack.io](http://techstacks.io/) and check out the most popular programming languages, databases and libraries that are being used today. However, these are the results and statistics that others have done for you, what about creating one by ourselves? What does it mean by creating one by ourselves? 

This project is still a WIP data mining project which aims to crawl the companies/jobs listings on this [stackoverflow page](http://stackoverflow.com/jobs/companies) to get a feel of the trend of technologies. Rougly, the basic flow would be:

1. Grab names of technologies within the tech section in a company listing and save it to a local database
2. Do data cleaning/analyzing
3. Present the result on a web page with data visualization

Right now I am utilizing the [scrapy](http://scrapy.org/) framework to do the first step. As for the database, currently considering using Redis.


(README in progress) 
