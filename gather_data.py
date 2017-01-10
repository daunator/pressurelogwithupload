#!/usr/bin/env python

from array import array
import os
import Adafruit_BMP.BMP085 as BMP085

dir_name = os.path.dirname(os.path.realpath(__file__)) + '/data/'

def get_data():
  sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)
  temperature = sensor.read_temperature()
  pressure = sensor.read_pressure() / 100.0  # conversion to hPa
  return temperature, pressure

def write_value_to_file(file_name, value):
  with open(file_name, 'ab') as file:
    float_array = array('d', [value])
    float_array.tofile(file)

if __name__ == '__main__':
  temp, pressure = get_data()
  write_value_to_file(dir_name + 'temp.bin', temp)
  write_value_to_file(dir_name + 'pressure.bin', pressure)

