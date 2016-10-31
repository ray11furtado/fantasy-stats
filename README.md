# fantasy-stats

When making a new emailer 
specifiy the service with either gmail, yahoo, outlook or hotmail
EX

email = emailer('gmail')

to login needs the email and password

email.login('myEmail@gmail.com', 'myPassword')

To send email with text:

email.send('ToThisEmail@gmail.com',  'MySubjectLine', "MyText")

For NBA stats

specify start day and how many days after that 
the first start day will be 1, as NBA season goes on more days will be available.

kobe(1,0) This will only get the first day of stats.

Now we want to get the data, you have the option of specifying a minmum amount of minutes to get players with significant amount of minutes

kobe.getData(20)

Once we have our data we want to write a CSV file
To do this simply just add the name of the file

kobe.writeToCsv('day1_stats')