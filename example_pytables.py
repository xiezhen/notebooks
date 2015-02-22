# coding: utf-8
import tables
help(tables.openFile)
h5f = tables.openFile('test.h5','w',title='Hi')
print h5f
h5f.createGroup('/','box')
print h5f
import numpy as np
data = np.arange(24).reshape((8,3))
print data
grid = h5f.createArra('/box','grid',data)
grid = h5f.createArray('/box','grid',data)
grid
grid.read()
grid[:]
grid[1,2]
array(5)
print h5f
for node in h5f:
    print node._v_pathname
    
h5f.root
h5f.root._v_attrs
h5f.root._v_attrs.author="Ivan"
h5f.root._v_attrs.keywords=np.array(["sample","data"])
h5.root._v_attrs
h5f.root._v_attrs
h5f.close()
get_ipython().magic(u'save pytables_1.py')
get_ipython().magic(u'save pytables_1.py 1-25')
from tables import *
class SensorMeasurement(IsDescription):
    id = Int64Col(pos=0)
    pos = Float32Col(shape=3, pos=1)
    tstart = Time32Col(pos=2)
    tstop = Time32Col(pos=3)
    kind = StringCol(itemsize=16, dflt="temperature",pos=4)
    value = FloatCol(pos=5)
    
h5f = openFile('Sensors.h5','a')
sensors = h5f.createTable('/','sensors',SensorMeasurement)
sensors
newrow = sensors.row
for i in range(6):
    newrow['id']=i
    newrow['pos']=(9*i,-18*i,500*i)
    newrow['value']=30+i
    newrow.append()
    
sensors.flush()
sensors
def print _sensors(s):
    for row in s:
        k, v = row['kind'], row['value']
        h = row['pos'][2]
        print "%s sensor at %g m, value %g"%(k,h,v)
        
def print_sensors(s):
    for row in s:
        k, v = row['kind'], row['value']
        h = row['pos'][2]
        print "%s sensor at %g m, value %g"%(k,h,v)
        
print _sensors(sensors)
print_sensors(sensors)
for row in sensors:
    row['value'] *= 1.5
    row.update()
    
sensors.flush()
print_sensors(sensors)
sensor[:3]
sensors[:3]
sensors[1::2]
data = sensors[:]
sensors[-2:] = data[:2]
sensors[:]
sensors.cols.value
sensors.cols.value[:]
sensors.cols.value[:5]
sensors.cols.value[:5] = range(5)
sensors.cols.value[:5]
sensors.append(data)
sensors[:]
bigsensors = h5f.root.bigsensors
sensors.nrows
sensors.nrows*sensors.rowsize
print_sensors(sensors[-10:])
print_sensors(r for r in sensors if r['value']<35)
c = '(kind == "wind speed") & (value >100) & (tstop-tstart<120)'
print_sensors(sensors.where(c, stop=1000000))
