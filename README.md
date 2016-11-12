# GmailFilter
Create file xml

## Simple script generate XML file.

### List of emails
```
example@example.com
example2@example2.com.br
```

### Execute command.

`python gmailfilter.py`

### Result XML File
```
<?xml version='1.0' encoding='UTF-8'?>
 	<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>

	<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id></id>
		<updated></updated>
		<content></content>
		<apps:property name='hasTheWord' value='example@example.com'/>
		<apps:property name='shouldTrash' value='true'/>
	</entry>
</feed>
```
