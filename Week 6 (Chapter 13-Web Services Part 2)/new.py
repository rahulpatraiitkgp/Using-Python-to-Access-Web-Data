import urllib2
import json

url = raw_input("Enter json URL: ")
connection = urllib2.urlopen(url)
raw_data = connection.read()
parsed_data = json.loads(raw_data)
counts = []

comments = parsed_data["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))