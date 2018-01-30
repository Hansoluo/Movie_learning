# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def movie_info(url):
	'''输入豆瓣电影页面链接，获取电影名，导演，演员，类型和地区'''
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "lxml")
	title = soup.find("h1").get_text().strip().split("\n")[0]
	info = soup.find("",{"id":"info"}).get_text().strip().split("\n")
	director = info[0].split(":")[1].split("/")[0].strip()
	actor0 = info[2].split(":")[1].split("/")[0].strip()
	actor1 = info[2].split(":")[1].split("/")[1].strip()
	genre0 = info[3].split(":")[1].split("/")[0].strip()
	genre1 = info[3].split(":")[1].split("/")[1].strip()
	country = info[4].split(":")[1].split("/")[0].strip()
	return [title, director, actor0, actor1, genre0, genre1, country]

i = []

def get_movie():
	url =  input("请输入豆瓣电影页面网址链接：")
	i = movie_info(url)
	print("您输入的电影为：{}\n导演：{} \n演员：{} {}\n类型：{} {}\n上映地区：{}".format(
			i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

if __name__ == '__main__':
 	main()