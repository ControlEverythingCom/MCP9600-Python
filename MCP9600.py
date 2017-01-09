import smbus
import time

address = 0x64

bus = smbus.SMBus(1)

bus.write_byte_data(address, 0xC0, 0x00)

time.sleep(0.5)

bus.write_byte(address, 0xC1)

time.sleep(0.5)

data0 = bus.read_byte(address)

data1 = bus.read_byte(address)

if((data0 & 0x80) == 0x80):
  data0 = data0 & 0x7F
  temp = 1024 - (data0 * 16 + data1/16)
  temp = (temp * 1.8)+32
  print temp
else:
  temp = data0 * 16 + data1/16
  temp = (temp * 1.8)+32
  print temp
