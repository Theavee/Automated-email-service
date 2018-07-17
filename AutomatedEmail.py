#Avee Chakraborty,151-35-924,department of software engineering,DIU.

import smtplib

#for establishing a connection , parameters are domain name and port
object_of_smtp = smtplib.SMTP('smtp.gmail.com',587)

#send a simple hello message

object_of_smtp.ehlo()
#starting TLS encription
object_of_smtp.starttls()
#login requires personal email and password
object_of_smtp.login('swe@gmail.com','password')
#message goes from -> to -> message 
object_of_smtp.sendmail('swe@gmail.com','aveechakra@gmail.com','subject: Bangladesh. \nThe name of our country is bangladesh')
{}
#disconnecting from smtb server
object_of_smtp.quit()
