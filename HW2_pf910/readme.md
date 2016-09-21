
Pooneh Famili
pf910
Assignment1:
It asks us to read a json fie from MTA website and show the number of buses in a line and also its location and run in .py format with two arguments: key and bus line name. To doing so, first I asked MTA website to send me the key and then we have to import urllib to enable python to read the link we give it. Then we have to figure out about the address of vehicle location(latitude and longitude) for that we have to address them, and we have to find out in which dictionary and list these information exist. To print a of the locations of one line we have to know the number of buses in that line, so we put a for loop to read all of them and print it.
** In this assignment, Mona helped me, to learn about arguments.
Assignment2:
It asks us to have our output in csv file, and also run it in .py format. To doing so, we have 4 arguments: the name of the file, key, bus line name, and a csv file. Same as assign 1 we have to read data in json format and from that url link. Then we open a csv file that its headers are: number of buses, latitude, longitude, next stop, and stop status. 
Then we define a loop for the len of the existed address, also we put an if statement, to see if all the next stops and stop status have data in it otherwise give us N/A.
Then we write all the information in one line in csv and it goes to the end of the loop. At the end we close the csv file.
** In this statement, Jonathan help me about arguments, and also, Adriano.
Assignment3: 
For this problem we have to make a environmental variable called DFDATA, first we go to compute and vi .bashrc and we export and alias for DFDATA.
Then, we come back to note book and first print the environmental variable that we call it via os.getenv
Then we read the data in csv format, and drop the unwanted columns via drop. Then we convert the data in to float in order to plot it.
** In this problem Jonathan helped me and I also give some help to Adriano.
Extra Credit:
For this assignment, it asks us to find a csv file which one of them include date and then plot numerical column versus time/date. To do that, first we just choose two column that we want to use and put it in other data set then we call the columns to make sure about the names to know what exactly we have to call(spaces ,…). Then  we use pd_to_datetime to make it readable for pandas and then plot it.
** Ben helped me in this homework and I helped Adriano.
