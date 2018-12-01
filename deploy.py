import glob
import hashlib
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


class FileMD5(object):
	fileName: ''
	MD5: ''

	def __init__(self, file_name, md5):
		self.fileName = file_name
		self.MD5 = md5


list1 = []
list2 = []
firstcopy = glob.glob(sys.argv[1] + '/**/*.html', recursive=True)

if firstcopy.__len__() <= 0:
	print('No HTML file found!')
	exit(0)

for filename in firstcopy:
	with open(filename, 'rb') as inputfile:
		data = inputfile.read()
		list1.append(FileMD5(filename, hashlib.md5(data).hexdigest()))

while 1:
	secondcopy = glob.glob(sys.argv[1] + '/**/*.html', recursive=True)
	for filename in secondcopy:
		with open(filename, 'rb') as inputfile:
			data = inputfile.read()
			list2.append(FileMD5(filename, hashlib.md5(data).hexdigest()))
	if list1.__len__() == list2.__len__() == 0:
		print('Nothing to do')
		list2.clear()
		continue
	for filelist2 in list2:
		for filelist1 in list1:
			if filelist1.fileName == filelist2.fileName and filelist1.MD5 == filelist2.MD5:
				list2.remove(filelist2)
				if list2.__len__() == 0:
					continue
				pp.pprint(list2)
				pp.pprint(list1)
# TODO: Add check to see if we have to remove or add files
