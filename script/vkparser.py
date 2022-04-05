import vk 
import json


def groopapi(groop):
	posts = api.wall.get(domain=groop, count="1", offset="1")
	count = posts['count']
	print("Общее количество записей: " + str(count))
	for i in range(0, 10):
		print("Итерация: " + str(i))
		posts = api.wall.get(domain="govoritnikolsk", count="1", offset=i)
		print(json.dumps(posts, indent=4, ensure_ascii=False))


def groopsearch(searchstr):
	print("start")
	searchrezult = api.groups.search(q=searchstr)


if __name__ == "__main__": 
	token = "0ed3213a0ed3213a0ed3213a720ea8cf8600ed30ed3213a6c965dbb4a9cda1aeaaed320"  # Сервисный ключ доступа
	session = vk.Session(access_token=token)  # Авторизация
	api = vk.API(session, v="5.85")

	#groopapi("news_gorodvo")

	groopsearch("Николськ")



