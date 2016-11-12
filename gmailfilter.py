import sys
sys.stdout = open('mailFilters.xml', 'w')

# Header
print """<?xml version='1.0' encoding='UTF-8'?>
 	<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>""" 

# Content
with open('emails.txt') as file:
	content = file.readlines()

	for line in content:
		if line.rstrip() != '':
			
			entry = """
	<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id></id>
		<updated></updated>
		<content></content>
		<apps:property name='hasTheWord' value='{}'/>
		<apps:property name='shouldTrash' value='true'/>
	</entry>""".format(line.rstrip())

			print entry

# Footer
print "</feed>"