# Outline
  * The program uses requests and BeautifulSoup in order to track an Amazon product via a user inputted url that is validated and a target price. The program also accepts a mail id that is to be mailed if the product is below target price using the python smtplib module. The program repeats the process once a day. Detailed description below.

# Purpose
  * The program was built out of necessity as I wanted to track the price of a mechanical keyboard that I hoped to purchase once the price reached a certain level, thereby helping me produce a very useful product. While extremely engaging to code, the build allowed me to further solidify my understanding of BeautifulSoup and Web-Scraping while introducing me to automatic email via smtplib.

# Description
  * Built on the foundations of OOP, the program utilises a class PriceTracker that is given the url to track, target price and mail to send. This data is inputted from the user in the main() function.
  * The main function validates the user input for the url and target and creates an instance of the Class and excepts for a KeyboardInterrupt.
  * In the class, the constructor sets the class variables and establishes the SMTP connection.
  * The driver function uses a while loop and runs the check_price() function and then sleeps for a day.
  * The check_price parses the webpage and finds the price, converting it to float. If the price is below or equal to target, it calls the send_mail() function else it returns to the driver().
  * The send_mail() function formats the url, title and price in a message and sends this email to the smail provided, following which it calls sys.exit to quit.
