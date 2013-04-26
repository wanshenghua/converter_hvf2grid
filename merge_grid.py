#!python

#merge two grid files into a single file.
from __future__ import print_function
import sys, time

#print(len(sys.argv))

def countVertexHex(contents):
    n_vert = 0
    n_hex = 0
    for line in contents:
        if line[:6] == 'Vertex' :
            n_vert += 1 
        elif line[:3] == 'Hex' :
            n_hex += 1
    return [n_vert, n_hex]


contents_0 = []
with open(sys.argv[1], 'r') as f:
    contents_0 = f.readlines()

li_0 = countVertexHex(contents_0)
n_vert_0 = li_0[0]
n_hex_0 = li_0[1]

contents_1 = []
with open(sys.argv[2], 'r') as f:
    contents_1 = f.readlines()

li_1 = countVertexHex(contents_1)
n_vert_1 = li_1[0]
n_hex_1 = li_1[1]

#concatenate two files and change indices in 2nd file
for line in contents_0[:n_vert_0] :
    print(line, end='')

    
for line in contents_1[:n_vert_1] :
    items = line.split()
    new_vid = int(items[1]) + n_vert_0
    print(items[0] + ' ' + str(new_vid) + ' ' + items[2] + ' ' + items[3] + ' ' + items[4])

for line in contents_0[n_vert_0:]:
    print(line, end='')

for line in contents_1[n_vert_1:]:
    items = line.split()
    new_hid = int(items[1]) + n_hex_0
    new_vid0 = int(items[2]) + n_vert_0
    new_vid1 = int(items[3]) + n_vert_0
    new_vid2 = int(items[4]) + n_vert_0
    new_vid3 = int(items[5]) + n_vert_0
    new_vid4 = int(items[6]) + n_vert_0
    new_vid5 = int(items[7]) + n_vert_0
    new_vid6 = int(items[8]) + n_vert_0
    new_vid7 = int(items[9]) + n_vert_0
    print(items[0] + ' ' + str(new_hid) + ' ' + str(new_vid0) + ' ' + str(new_vid1)  + ' ' + str(new_vid2)  + ' ' + str(new_vid3)  + ' ' + str(new_vid4)  + ' ' +str(new_vid5)  + ' ' +str(new_vid6)  + ' ' + str(new_vid7))
#end
