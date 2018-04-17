# -*- coding:utf-8 -*-
# 格子乘法

M = 0
N = 0

#输入
M = map(int,list(raw_input()))
N = map(int,list(raw_input()))



#初始化格子矩阵 aList = [[0] * cols for i in range(rows)]!!!!!!
Lattice = [[[0]*2 for j in range(len(M))] for i in range(len(N))]

lenth = len(M)*len(N)
#print Lattice

#M:[1, 2, 3] 
#N:[1, 2, 3]
out_multi = [0]*lenth
out = []
multiply = []
def main():
	temp = 0
	for i in range(len(N)):		
		for j in range(len(M)):
			temp = N[i]*M[j]
			#print temp
			Lattice[i][j][0] = temp / 10
			
			Lattice[i][j][1] = temp % 10
			temp = 0
			#print Lattice_0[i][j],j,i
	#print Lattice[-1][2][1]
	lattice(Lattice)

def lattice(L_array):
	out.insert(0,L_array[len(N)-1][len(M)-1][1])
	turn_col = 1
	turn_raw = 0
	flag_col = 0
	sum = 0
	#计算格子矩阵右下部分
	for j in range(1,len(M)):
		sum = flag_col
		turn_col = 1

		for raw in range(j+1):
			for col in range(2):
				try:
					sum += Lattice[len(N)-1-raw][len(M)-1-j+raw+col][turn_col]
					#print '===',Lattice[len(N)-1-raw][len(M)-1-j+raw+col][turn_col]
					if turn_col == 1:
						turn_col = 0
					else:
						turn_col = 1
				except:
					break

		flag_col = sum / 10
		#print sum,flag_col
		sum = sum % 10
		out.insert(0,sum)
	
	#计算格子矩阵左上部分
	
	for i in range(len(N)-1):
		sum = flag_col
		turn_raw = 0
		for col in range(len(M)-i):
			for raw in range(2):
				try:
					if (len(N)-1-i-raw-col)<0:
						break
					sum += Lattice[len(N)-1-i-raw-col][col][turn_raw]
					#print '+++',Lattice[len(N)-1-i-raw-col][col][turn_raw]
					if turn_raw == 0:
						turn_raw = 1
					else:
						turn_raw = 0
				except:
					break
		#print sum 		
		flag_col = sum / 10
		sum = sum % 10
		out.insert(0,sum)
	Lattice[0][0][0] = Lattice[0][0][0]+flag_col
	out.insert(0,Lattice[0][0][0])
	#print out

	for i in range(len(out)):
		#print out[i]
		if out[i]>0:
			for j in range(i,len(out)):
				multiply.append(out[j])
			#print multiply
			break
		else:
			pass
	#print multiply
	print ''.join(map(str,multiply))

	
main()