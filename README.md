# Reminder

Basic reminder app I put together in a few hours in Python. This app is still in a very early stage of development, there many more features I have in mind that I plan to add to it in the future.

  
  

# Requirements

  

Check out the [requirements](https://github.com/haljadooa/reminder/blob/master/requirements.txt) file.

  

# Database

  

My database of choice is MySQL using [Laragon](https://www.laragon.org/download/), get the **WAMP** version, it's the only one that has MySQL. Laragon only works on windows however, so if you you're on [Mac OS](https://dev.mysql.com/doc/refman/5.6/en/osx-installation-pkg.html) or [Linux](https://dev.mysql.com/doc/refman/5.7/en/linux-installation.html)... follow the links for your respective OS.

  

if you want to use the exact database design I use, [Click Here](https://github.com/haljadooa/reminder/blob/master/database/) then download  `reminder.sql` after that install it which ever way you like. if you use HeidiSQL...

  

1. Click on "File" on the top left

2. Then Click "Run SQL File"

3. Navigate to the SQL file included with Reminder and Open it.

  

Finally update `app.py` with your database credentials. 

  

# Usage
In the `app.py` file...
 - Update  `PORT` with the port you want the server to run on.
 - Make sure your database details are correct.

If you followed the above instructions successfully, in your command line window run the `python app.py`command and navigate to `127.0.0.1:PORT_YOU_CHOSE_HERE` in your favorite browser.

note: if you want to access reminder from other devices in your home network, simply update `app.run()` to your local IP address. If you do know what your local IP address is[click here](https://www.whatismyip.com/). And make sure your firewall is either disabled or allows the site to send/receive traffic.

  
  

# Extra

  
  

This is my first semi-major project ever, so sorry if it sucks... but I have to start from somewhere :) This is alse my first README paper, so yeah... idk if it sucks or not, looks fine to me tbh.

  

Any and all improvements made to the code are welcome, best way for me to implement improvements you make is through the use of pull requests.
