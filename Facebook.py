__author__ = 'Rio Essed'

import facebook
from pprint import pprint


token = "CAACEdEose0cBALActPuiP6x8snRgZBrkK2c1AoTDhP0eWJxTCENQX7ZAP4eafdqnt24DNzjsPTvpDXuybvZCzEKcmd1K6wzE4Igx2ZAjg89kJR6Ehn6WnEwJefU0oBPUs4ZBirZA08uyphvgeGyRt0TFRLupYcv52bGD4jT0UsYzUsEVM1QqNZAkhXa9y4b5H4VVBlDunmppZCto7o5JqvRQN75fZCgbWW8YZD"
g = facebook.GraphAPI(token)

personalData = g.get_object("me")
myLikes = g.get_connections("me", "likes")['data']
myEvents = g.get_connections("me", "events")['data']
friendList = g.get_connections("me", "friends")['data']
friends = g.get_connections("me", "friends")['data']

data= {'personal': personalData, 'likes':myLikes, 'events': myEvents, 'friends':friendList }
#pprint (data)
        
def friendData(type):        
	for friend in friends:
		name = friend['name']
		friendid = friend['id']
		data = g.get_connections(friend['id'], type)['data']
		gender = g.get_object(friend['id'])['gender']
		#birthday = g.get_object(friend['id'])['birthday']
		#id = g.get_connections(friend['id'], "likes")['data'][0]

		for item in data:
			title = item['name']
			id = item['id']
			output = friendid + ";" + gender + ";" +  ";" + name + ";" + title + ";" + id
	
			#print name
			pprint(output)
	


friendData("likes")

	

#pprint(data)






