import urllib2


lines = [line.rstrip('\n') for line in open('../repo.txt')]
for line in lines[1:]:
	l = line.split(';')
	filename = l[1].split('/')[-1]
	print l[0]
	try:
		response = urllib2.urlopen(l[0])
		content = response.read()
		output = open(filename, 'w')
		output.write(content)
		output.close()
	except Exception, e:
		print str(e.reason)
