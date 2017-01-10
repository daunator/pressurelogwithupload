#!/usr/bin/env python

import requests, time, os
from array import array

dir_name = os.path.dirname(os.path.realpath(__file__)) + '/data/'

def log_error(message):
  with open(dir_name + 'error.txt', 'a') as file:
    time_now = time.strftime("%Y-%m-%dT%H:%M:%S")
    file.write('{} at: {}\n'.format(message, time_now))

def read_values_from_file(file_name):
  float_array = array('d')
  with open(file_name, 'rb+') as file:
    try:
      float_array.fromfile(file, 6)
    except EOFError:
      log_error('Less than 6 values read from ' + file_name)
    # clear file contents
    file.seek(0)
    file.truncate()
  
  return float_array.tolist()  

def upload_data(temperature, pressure):
  base_url = "http://data.sparkfun.com/input/"
  public_key = ***
  url = base_url + public_key
  private_key = ***
  temperature_str = "{:.1f}".format(temperature) # keep only 1 decimal
  pressure_str = "{:.2f}".format(pressure) # keep 2 decimals
  r = requests.post(url, headers={'Phant-Private-Key': private_key}, data = {'temperature':temperature_str, 'pressure':pressure_str})
  return r.status_code == requests.codes.ok

if __name__ == '__main__':
  temp = read_values_from_file(dir_name + 'temp.bin')
  pressure = read_values_from_file(dir_name + 'pressure.bin')
  if not len(temp) or not len(pressure):
    log_error('Error no data')
  else:  
    temp_average = sum(temp) / float(len(temp))
    pressure_average = sum(pressure) / float(len(pressure))
    result = upload_data(temp_average, pressure_average) # Celsius and hPa
    if not result:
      log_error('Error uploading data')

