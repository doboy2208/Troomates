__author__ = 'Rio Essed'

import json
import urllib2
from pprint import pprint

tempurl = 'https://api.spotify.com/v1/me/tracks?offset='
bearer_token = 'BQBt-np8B0JQrxNSGbVVVB-SgHTinMGDfdIr1zGfiEEiEICtjbbbcnBu8w8S0XTmL4CfP4sqHrkupBY0SDEy9JfD1LMa-ZtQC0SuHykRsKOiXV_Ya_Fj9YCcDed2BDQbX8XqnDhOTZ12aDzID6bQzfQ9oUZu_g2cS4Vd1J2ITjbr6qY'
agent = 'Spotify API Console v0.1'

def getSpotifyTracks(tempurl, bearer_token, agent):
	outputList =[]
	req = urllib2.Request(tempurl+"0")
	req.add_header('Authorization', 'Bearer '+ bearer_token + '')
	req.add_header('User-Agent', agent)
	req.add_header('Accept', 'application/json')
	req.add_header('Content-Type', 'application/json')
	response1 = urllib2.urlopen(req)
	data = json.loads(response1.read())
	total = data['total']
	c= 0
	while c< total:
		url = tempurl + str(c)
		req = urllib2.Request(url)
		req.add_header('Authorization', 'Bearer '+ bearer_token + '')
		req.add_header('User-Agent', agent)
		req.add_header('Accept', 'application/json')
		req.add_header('Content-Type', 'application/json')
		response1 = urllib2.urlopen(req)
		data = json.loads(response1.read())['items']
		c = c+20
		for item in data:
			trackName = item['track']['name']
			albumName = item['track']['album']['name']
			artists = item['track']['artists']
			trackID = item['track']['id']
			for item in artists:
				artistName = item['name']
				artistID = item['id']
				url = 'https://api.spotify.com/v1/artists/' + artistID
				req = urllib2.Request(url)
				response1 = urllib2.urlopen(req)
				data = [json.loads(response1.read())]
				for item in data:
					genre = str(item['genres'])
			output = trackID + ";" + trackName + ";" + artistID + ";" + artistName + ";" + genre
			outputDict = {'trackid' : trackID, 'trackname' : trackName, 'artistID' : artistID, 'artistname' : artistName, 'genre' : genre}
			outputList.extend([outputDict]) 
			file=open('usertracks.txt', 'a+')
			pprint(output, file)
						
def getUserData():
	url = 'https://api.spotify.com/v1/me'
	bearer_token = 'BQCYUxawO23uwL8ZEtGDrgvf-vbhWg0EYQaQQOCp_fj-S1eWQwF7gqLN03jxN6QuS6HewGVPsCrVQHVMJLq_QXPP57UHtahA6IqZXtLTlZYBXFmztFGP6NQVqdGkgS9X0NiQReiPTOIHCag9raWe2JRmf2G4zlA-yGznLZ1xH7_MGUI'
	agent = 'Spotify API Console v0.1'

	req = urllib2.Request(url)
	req.add_header('Authorization', 'Bearer '+ bearer_token + '')
	req.add_header('User-Agent', agent)
	req.add_header('Accept', 'application/json')
	req.add_header('Content-Type', 'application/json')
	response1 = urllib2.urlopen(req)
	data = json.loads(response1.read())
	name = data['display_name']
	birthday = data['birthdate']
	email = data['email']
	spID = data['id']
	profileURL = data ['external_urls']['spotify']
	
	output = spID + ";" + name + ";" + email + ";" + birthday + ";" + profileURL
	outputDict = {'userspid' : spID, 'username' : name, 'useremail' : email, 'userbirthday' : birthday, 'profileurl' : profileURL}
	
	file=open('userdata.txt', 'a+')
	pprint(output, file)
	
getSpotifyTracks(tempurl, bearer_token, agent)

#getUserData()