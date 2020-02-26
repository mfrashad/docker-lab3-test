import wikipedia
import sys


page = wikipedia.page(wikipedia.search(sys.argv[-1])[0])
links = []

for link in page.links:
	links.append({"page":link})
	
for link in links:
	print("{}").format(link["page"])