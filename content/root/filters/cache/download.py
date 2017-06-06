import urllib2


lines = [line.rstrip('\n') for line in open('../../../../api/v1/prod/filters')]
for i in range(0, len(lines), 8):
	entry = lines[i:i + 8]
	name = entry[1]
	url = entry[6]
	print name
	try:
		response = urllib2.urlopen(url, timeout=10)
		content = response.read()
		output = open(name, 'w')
		output.write(content)
		output.close()
	except Exception, e:
		print str(e.reason)
