# mangafox_scrapper
A scrapper to scrap any manga from mangafox.me

Aim : To Download any manga from mangafox.me
Requirements : BeautifulSoup ,Requests ,python 2.7
platform : Currently tested for linux (Tested on Debian wheezy ,suse 13.2)

Instructions :

Use pip to download BeautifulSoup and requests.
script can be run by cd into the folder containing script and using command :
python mangafox_a

You should get the name as exactly as shown in url of mangafox.me
for eg : http://mangafox.me/manga/one_piece/
here "one_piece" is the name you have to enter when prompted for the name of series.

This script mantains a log which can be used to continue the download in case of failure.

Feedback is welcomed :)

further plans:
multiprocessing,to speed up the process.
