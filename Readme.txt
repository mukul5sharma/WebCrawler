Assignment 1

Mukul Sharma
sharma.mu@husky.neu.edu


Description of files in zip folder
1. webCrawler.py : File containing the main crawler code

2. unFocussedurls.txt : File containing the urls crawled 
			without using the keyphrase

3. focussedurls.txt : File containing the urls crawled 
		      using the keyphrase "concordance"

4. Readme.txt : Description of files and instruction on running the
		program.



Program execution instructions :

1. Prerequisites : python 2.7 with beautifulsoup package installed

2. The program takes 2 arguments -
	(i)  The seed url [command : python webCrawler.py "seed url"]
	(ii) The keyphrase (optional) [command : python webCrawler.py "seed url" "keyphrase"]


Q. what proportion of the total pages were retrieved by the 
   focused crawler for ‘concordance’
Answer :
   1.Total pages crawled while searching for keyphrase = 13471
   2.Total pages where the keyphrase was found = 254

   So, total proportion = 0.0188




