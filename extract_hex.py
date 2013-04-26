#!python
#python2.7
import sys

contents = []
with open(sys.argv[1], 'r') as f:
    contents = f.readlines()

dimension = contents[0].split()
dimension
dim_0 = int(dimension[0])
dim_1 = int(dimension[1])
dim_2 = int(dimension[2])

#map i,j,k to a point
map2pt = {}
pt_id = 0 #index to a point
for i in range(0, dim_0):
    for j in range(0, dim_1):
        for k in range(0, dim_2):
            index = str(i) + ' ' + str(j) + ' ' + str(k)
            map2pt[index] = pt_id
            print('Vertex ' + str(pt_id) + ' ' + contents[pt_id + 1].rstrip())
            pt_id += 1

hex_id = 0
for k in range(0, dim_2 - 1):
    for j in range(0, dim_1 - 1):
        for i in range(0, dim_0 - 1):
            ind0 = str(i) + ' ' + str(j) + ' ' + str(k)
            ind1 = str(i) + ' ' + str(j) + ' ' + str(k + 1)
            ind4 = str(i + 1) + ' ' + str(j) + ' ' + str(k)            
            ind5 = str(i + 1) + ' ' + str(j) + ' ' + str(k + 1)            
            ind2 = str(i) + ' ' + str(j + 1) + ' ' + str(k) 
            ind3 = str(i) + ' ' + str(j + 1) + ' ' + str(k + 1) 
            ind6 = str(i + 1) + ' ' + str(j + 1) + ' ' + str(k)
            ind7 = str(i + 1) + ' ' + str(j + 1) + ' ' + str(k + 1)             
            pt_id0 = map2pt[ind0]
            pt_id1 = map2pt[ind1]
            pt_id2 = map2pt[ind2]
            pt_id3 = map2pt[ind3]
            pt_id4 = map2pt[ind4]
            pt_id5 = map2pt[ind5]
            pt_id6 = map2pt[ind6]
            pt_id7 = map2pt[ind7]
            print( 'Hex ' + str(hex_id) + ' ' + str(pt_id0) + ' ' + str(pt_id1) + ' ' + str(pt_id2) + ' ' + str(pt_id3) + ' ' + str(pt_id4) + ' ' + str(pt_id5) + ' ' + str(pt_id6) + ' ' + str(pt_id7))
            hex_id += 1
#end
