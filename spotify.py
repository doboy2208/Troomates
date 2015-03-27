__author__ = 'Rio Essed'

import json
import urllib2
from pprint import pprint

tempurl = 'https://api.spotify.com/v1/me/tracks?offset='
bearer_token = 'BQAGwVV3rQiEP48so8L9zxJFT8s31w3bnS6lBQkkwmX98w9Ce25uAhz2All4cgqLcd2YA98tVdOrDHgHTW7KO-VoC9S7uEhFcNLIjhHwVSC3w0JNXkUOx3FZ73eLxH3TKmGHNWxiwx-j6qweg6CL'
agent = 'Spotify API Console v0.1'

def getSpotifyTracks(tempurl, bearer_token, agent):
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
			file=open('output.txt', 'a+')
			#pprint(output, file)
			pprint(output)
						
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
	pprint(output)
	
getSpotifyTracks(tempurl, bearer_token, agent)

getUserData()