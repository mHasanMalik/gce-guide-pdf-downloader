import requests
from bs4 import BeautifulSoup
import urllib2, urllib


def get_all_links(URL):
	req = requests.get(URL)
	href_links = []
	if req.status_code == 200:
		parser_obj = BeautifulSoup(req.content, "html.parser")
		tr_tag_lists = parser_obj.find_all('tr', {'class', 'file'})
		for tag in tr_tag_lists:
			all_a_tag = tag.find_all("a", {"class": "name"})
			for a_tag in all_a_tag:
				href_links.append(a_tag["href"])
				print a_tag
			#href_links.append(a_tag["href"])
	else:
		print "Bad status code! Check internet connection"	
	return href_links
	



def download_files(URL, href_links):
	
	for href in href_links:
		req = requests.get("%s/%s" % (URL, href), stream= True)
		if req.status_code == 200:
			link = "%s%s" % (URL,href)
			r = requests.get(link, stream = True)
			filename = href
			
			with open(filename, 'wb') as f:
            			for chunk in r.iter_content(chunk_size = 1024*1024):
               				if chunk:
                    				f.write(chunk)
	

			print "%s downloaded!\n"%filename				
			
			#try:
			#	urllib.urlretrieve(link, filename)			
			#except:
			#	print "Error 404: Couldnt download file"
				
			#print "Full link is active"
			#print "%s%s" % (URL, href)
	



def main():
	URL = "https://papers.gceguide.com/O%20Levels/D-Maths%20(4024)/"
	a_tag_list = get_all_links(URL)	
	#for url in url_list:
	#	print "%s" % url
	download_files(URL,a_tag_list)
	
	
	
if __name__ == "__main__":
	main()
