from PIL import Image
import numpy as np
import scipy.misc
import textwrap
import bitarray
import sys

def printimage(l,w):
	for i in range(1):
		for j in range(w):
			print('{:<20}'.format(image.load()[i,j])),
		print('\n')
	print "--------------------------"

def bit2str(s):
	message = ""
	while s != "":
	    i = chr(int(s[:8], 2))
	    message = message + i
	    s = s[8:]
	return message

def update(l,w):
	print "max size of msg = %s"%((l-1)*w*3/8)
	print "Your msg : "
	try:
		msg = raw_input()
	except EOFError:
		print "Invalid msg"
		return
	ba = bitarray.bitarray()
	ba.frombytes(msg.encode('utf-8'))
	index=0
	l = len(msg)
	l2 = l
	for j in range(0,20):
		if l2==0 or l2%2==0:
			tp = image.load()[0,j][2]&~(1)
		else:
			tp = image.load()[0,j][2]|1
		l2 = l2/2
		image.load()[0,j] = (tp, tp, tp)

	for i in range(1,l):
		for j in range(w):
			tp = []
			for k in range(0,3):
				if index<l*8 and ba[index]:
					tp.append(image.load()[i,j][k]|1)
				else:
					tp.append(image.load()[i,j][k]&~(1))
				index = index+1;
			image.load()[i,j] = (tp[0],tp[1],tp[2])
			if index>=l*8 : 
				return
	return 

def getmsgfromimage(l,w):
	l = 0
	mul = 0
	for j in range(0,20):
		if(image.load()[0,j][2]&1):
			l = l + pow(2,mul)
		mul = mul+1
	index=0
	ba = ""
	print "msg size from pic is : " + str(l)
	for i in range(1,l):
		for j in range(w):
			for k in range(0,3):
				if index==l*8:
					return bit2str(ba)
				if (image.load()[i,j][k]&1):
					ba = ba + '1'
				else:
					ba = ba + '0'
				index = index+1
	
	return bit2str(ba)

save1 = sys.argv[1]
try:
	save2 = sys.argv[2]
except:
	save2 = save1

image = Image.open(save1)	

case = raw_input("1 - Update\n2 - Decode\ninput : ")
if (case=='1'):
	update(image.size[0],image.size[1])
elif (case=='2'):
	msg = getmsgfromimage(image.size[0],image.size[1])
	print "msg is : " + msg
else:
	exit(0)
image.save(save2, save2.split(".")[1].upper())


























'''open image and convert to writable array
image = Image.open("testimage.jpeg", mode="r")
idata = np.asarray(image)
idata.setflags(write=1)
print idata[0][0]
idata[0][0][1] = 6
print idata[0][0]
print type(idata)
scipy.misc.imsave('testimage.jpeg', idata)


image = Image.fromarray(idata,'RGB')
image.save('testimage', 'JPEG')

image2 = Image.open("test")
idata2 = np.asarray(image2)
print idata2[0][0]

#for c in dir(image):
#	print ("%s ==>> %s\n" % (c, getattr(image, c)))


#print repr(image.__array_interface__['data'])
image.__array_interface__['data'] = 45
print repr(image.__array_interface__['data'])
'''
