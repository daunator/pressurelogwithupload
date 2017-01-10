# pressurelogwithupload
Pressure and temperature logging every hour and upload the data to data.sparkfun.com

The functionality is devided into two files: gather_data.py and upload_data.py. These scripts are invoked automaticaly from crontab. The entries in crontab:
```
# m h  dom mon dow   command
*/10 * * * * /home/pi/code/sparkfun_logger/gather_data.py
5 * * * * /home/pi/code/sparkfun_logger/upload_data.py
```
First you need to install Adafruit Python library from https://github.com/adafruit/Adafruit_Python_BMP.git

Then put the public and private keys into upload_data.py
