# iatv-research

Web app for doing research with the Internet Archive's TV News Archive. Provides a CSV
version of search results from the TV News Archive's Advanced Search functionality.

How to use it:

Go to the Internet Archive's awesome TV News Archive at http://archive.org/details/tv, and then 
create a custom query using the Advanced Search functionality. When your search has been
specified and you want to export the results to a CSV, select and copy the URL which has the search query in it
from archive.org, go to http://iatv-research.com, and paste the query in the search box, then press Go. 
This will trigger the app to download the JSON result from the Archive, convert it to CSV, and 
send the CSV in response to your browser.

Here is an example search query I made searching for Hannity mentioning ambassadors from August, 2018 to today:
https://archive.org/details/tv?q=ambassador&red=1&and[]=publicdate%3A%5B2018-08-01-18+TO+2019-11-04%5D&and[]=creator%3A%22foxnewsw%22&and[]=program%3A%22Hannity%22
