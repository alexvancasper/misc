Misc

The proxy_checker.py can help to check proxies servers. It's getting them from site: http://www.ip-adress.com/proxy_list/ after that the script is checking each proxy server and then show only working proxy servers.

Example output: 
Requsting url: http://www.ip-adress.com/proxy_list/ 
Request from the server was recevied 
Got: 50 proxies 
1: Checking:
<...skip...> 
50: Checking: 
Checked: 43 proxies are working 
Writing to file 
Amount:43 Done


### INN_checker.py
Пример работы скрипта. 
***
```bash
$ ./nalog.py 
Enter the captcha: 006152
[1] Requesting INN: 7743541323	Captha: 006152
[1]	Total rows: 1
[1]	[1] PDF downloaded size: 125995 
Enter the captcha: 124515
[2] Requesting INN: 7743928560	Captha: 124515
Captcha is not correct, need to repeat! INN: 7743928560
Enter the captcha: 042174
[2] Requesting INN: 7743928560	Captha: 042174
Captcha is not correct, need to repeat! INN: 7743928560
Enter the captcha: 400801
[2] Requesting INN: 7743928560	Captha: 400801
[2]	Total rows: 1
[2]	[1] PDF downloaded size: 104479 
Enter the captcha: 234630
[3] Requesting INN: 7751000543	Captha: 234630
[3]	Total rows: 1
[3]	[1] PDF downloaded size: 112536 
```
Скрипт должен помочь бухгалтерам :)
