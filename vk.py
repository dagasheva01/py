import requests
# 77015209278 Kbtu2017!
# https://vk.com/dev
# https://vk.com/dev/methods
# https://vk.com/dev/manuals
# https://vk.com/dev/first_guide

# https://vk.com/dev/users.get
screen_name = 'alenkashishkova'
url = "https://api.vk.com/method/users.get?user_ids=%s" % screen_name
r = requests.get(url)
data = r.json()

print(data)

last_name = data['response'][0]['last_name']
first_name = data['response'][0]['first_name']
uid = data['response'][0]['uid']


url = "https://api.vk.com/method/users.get?user_ids=%s&fields=followers_count,last_seen" % screen_name
r = requests.get(url)
data = r.json()


user = data['response'][0]
if "last_seen" in user:
	time = user['last_seen']['time']

# https://vk.com/dev/friends.get

url = "https://api.vk.com/method/friends.get?user_id=%s&fields=followers_count,last_seen" % uid
r = requests.get(url)
data = r.json()
users = data['response']
top_count = 0
for user in users:
	if "followers_count" in user:
		followers_count = user['followers_count']
		if followers_count > 5000:
			top_count = top_count + 1
print(top_count)




