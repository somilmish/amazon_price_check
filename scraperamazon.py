import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Sony-WI-C200-Wireless-Neck-Band-Headphones/dp/B07S13PJ3W/ref=lp_6314131031_1_1?s=electronics&ie=UTF8&qid=1563542975&sr=1-1'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()

try:
	price = soup.find(id="priceblock_dealprice").get_text()
except: 
	price = soup.find(id="priceblock_ourprice").get_text()


# def convert_price():
# 	'''
# 		This converts the price from the weird formatting to an actual int
# 	'''
# 	split_price = price.split(',')
# 	last_of_first = split_price[0][-1]
# 	price_with_dot = last_of_first + split_price[1]
# 	converted_price = int(price_with_dot.split('.')[0])

def conversion():
	'''
	For conversion to int of the price.
	'''
	#price = '1,123,432,890.21'
	#x = price.split()[0].split(',')
	x = price.split()[1].split(',')
	num = 0

	for index, val in enumerate(x):
		if index == len(x)-1:
			y = int(val[:-3])
		else:
			y = int(val)
		num = num*1000 + y

	return num

converted_price = conversion()


def send_mail():
	'''
	Function to send email to the user. 
	'''
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('rossgay4chandler@gmail.com', 'chandramahesh1!')
	subject = 'Price fell down!'
	body = 'Check the amazon link https://www.amazon.in/Sony-WI-C200-Wireless-Neck-Band-Headphones/dp/B07S13PJ3W/ref=lp_6314131031_1_1?s=electronics&ie=UTF8&qid=1563542975&sr=1-1'
	msg = f"Subject: {subject}\n\n{body}"
	server.sendmail(
		'rossgay4chandler@gmail.com',
		'thermionicpositron@gmail.com',
		msg)
	server.quit()


required_price = 2200
if(converted_price < required_price):
	send_mail()
	print('Email has been sent successfully!')




