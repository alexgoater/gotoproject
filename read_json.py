# /usr/bin/env python

import json

name = '/Users/alex/Documents/Advanced Research Project/Python/GW170817.json'

with open(name) as json_file: 
     data = json.load(json_file) 

info = data['GW170817']['photometry']

ind = []

for i in info: 
    if 'magnitude' in i: 
        ind.append(i) 

mag = []
time = []
band = []

for i in ind: 
     mag.append(float(i['magnitude']))  
     time.append(float(i['time']) ) 
     band.append(i['band'])

all_r=numpy.where(band=='r')

mag_r = mag[all_r]
time_r = time[all_r]

numpy.savez('data_GW170817_from_json.npz', time=time_r, mag=mag_r)
