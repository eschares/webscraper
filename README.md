# webscraper

Trying to figure out how to create a webscraper using Python and Beautiful Soup to parse a page that shows an academic research article from Wiley.

https://onlinelibrary.wiley.com/doi/abs/10.1111/1744-7917.12600

I want it to pull the author list and see which one is the Corresponding Author (as denoted by the envelope icon, so Bonning in this case). Eventually, I will have a whole list of DOIs that I want to programmatically go out and record the author lists and their university, but for now I will just take the list of authors. I don't even want the full text of the article, just the landing page with the metadata information.

I first ran into a problem where Wiley denied me access, so I added the User-Agent headers and at least got a response. However, all my findAll's were coming back as 0's, so I printed the soup into a text file to inspect, and when I open the text file, I seem to be getting back some sort of filtered or encoded HTML. I can inspect the webpage in Chrome and see the divs, but my page_soup instance doesn't look like that. Full output at: https://gofile.io/d/4LYRTv
