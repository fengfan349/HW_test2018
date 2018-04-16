# -*- coding:utf-8 -*-
# 暴力搜索版本 ^_^
N = int(raw_input())
in_arr = [0]*N

for i in range(N):
	in_arr[i] = int(raw_input())

d = {}
k = 0

def main():
	try:
		search_route(0,0)
		print min(d.values())
	except:
		print "No jump,Check Input data!"

def search_route(id,jump_sum):
	for i in range(in_arr[id]):
		k = jump_sum
		if (i + id+1) == (N-1):
			k += 1
			d.setdefault(len(d)+1,k)	
		elif (i + id + 1) > (N-1):
			pass	
		else:
			k += 1
			search_route(id+i+1,k)

main()		