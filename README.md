# python-selenium-xpath-checker
Simple utilite to double-check yourself while using Selenium Driver for crawling websites.

Run this code in terminal, just need to input the website and the xpath. The log is saved into generated CSV file in the same folder.

The utilite is written and tested on mozilla/geckodriver https://github.com/mozilla/geckodriver/releases

You can play with firefox profile by uncommenting some preferences (the whole list http://kb.mozillazine.org/Category:Preferences):
 +To change the language ("en", "ru", "fr" ..):  firefox_profile.set_preference('intl.accept_languages', 'ru'); <br>
 +Display/not to display pics:                   firefox_profile.set_preference('permissions.default.image', 2); <br>
 +Download and display flash animation:          firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false'); <br>
 +To switch user-agent to "mobile" view:         firefox_profile.set_preference('general.useragent.override', 'Mozilla/5.0 (Linux; Android 7.0)      AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36')

Extra:
+ Utilite checks the time to upload webpage, it is not very accurate but helps if you have no idea which implicit waits you want to use in the future.
+ Future development: include the parsing of robots.txt file, include check for honeypots.

python 3.7.0
geckodriver 0.23.0
