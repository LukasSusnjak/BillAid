# BillAid

What does it do?
  The program web-scrapes the website of HNB(Hrvatksa Narodna Banka) for the value of Euro on current date, then it copies the value and adds it into a defined cell  
  in a spreadsheet program. 
  
How does it work? 
  The program combines the two useful and popular web-scraping tools to get the needed value from the site. It uses "Beautiful Soup 4" and "Selenium". Then it opens 
  the spreadsheet file named test.xlsx and it pastes the cell L16
  
How do I use it?
  It's simple, you have to save your reciept as test.xlsx in the same folder where the code is, and then you run it throught the terminal with command: 
  python3 bill.py 

IMPORTANT NOTE: Before using this program make sure you have python version 3 or later installed and that you have installed beautiful soup and selenium using pip. 
                It is possible that the code is buggy and that you might have to modify it since it is still in Beta Version. To change the cell in which you want 
                to save the value just replace l16 with the cell you need(in the line 26 of code: cellFix = sheet['l16']
                
                
