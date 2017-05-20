import requests
uid = '153429560'
url = 'https://api.vk.com/method/users.get?user_ids=%s&fields=status,last_seen,blacklisted,home_town&name_case=dat'
r = requests.get(url % uid)
data = r.json()
uid = data['response'][0]['uid']
url = 'https://api.vk.com/method/wall.get?owner_id=%d' % uid
print(url)
r = requests.get(url)
data = r.json()
response = data['response']
post_count = response[0]
posts = response[1:]
for post in posts:
	text = post['text']
	likes_count = post['likes']['count']
	comments_count = post['comments']['count']
	reposts_count = post['reposts']['count']
	if 'attachment' in post:
		if 'photo' in post['attachment']:
			photo_url = post['attachment']['photo']['src']
			print(photo_url)
	print(likes_count)