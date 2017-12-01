# Credits Dynamic Algorithm: https://github.com/devlinjunker/courses-max-subarray/blob/master/max-sub.py
# Credits Div and Conquer Algorithm: Dhawal Patel - Programming forum

import time
import sys

####################################################
def enumeration(A):
	max_subset = 0
	index_inicio = index_fim = 0

	for i in range(0,len(A) + 1):
		for j in range(i,len(A) + 1):
			soma = sum(A[i:j])
			if soma > max_subset:
				max_subset = soma
				index_inicio = i
                index_fim = j

	return max_subset
####################################################
def CrossingSum(arr,l,m,h):
    summ = 0
    left_sum = -sys.maxint
    for i in range(m,l-1,-1):

            summ = summ + arr[i]
            if summ > left_sum:
                    left_sum = summ


    summ = 0
    right_sum = -sys.maxint
    for i in range(m+1,h+1):
            summ = summ + arr[i]
            if summ > right_sum:
                    right_sum = summ

    return left_sum + right_sum

def Divide(arr,l,h):
    if l ==  h :
            return arr[l]
    mid = (l+h)//2
    maximum = max(Divide(arr,l,mid) , Divide(arr,mid+1,h) , CrossingSum(arr,l,mid,h))

    return maximum



####################################################
def dynamic(A):
    start = 0
    end = 0
    max_subset = 0

    vals = [0 for x in range(len(A))]

    for i in range(len(A)):
        if(i == 0):
            if(A[i] > 0):
                vals[i] = A[i]
        elif(A[i] + vals[i-1] < 0):
            vals[i] = 0
        else:
            vals[i] = vals[i-1]+A[i]
        

    for i in range(len(A)):
        if(vals[i] > max_subset):
            max_subset = vals[i]
            end = i+1

    temp = max_subset
    for i in reversed(range(end)):
        if(temp <= 0):
            start = i+1
            break
        else:
            temp = temp - A[i];

    return max_subset

####################################################


def gerarArray():
	f = open("../../entradas.txt", "r")
	fw = open("Python_Saidas.txt","w")
	for line in f:
		if "n = " in line:
			print "------------------------\n"
			print line
			fw.write(line)

			array = f.next().split('\n')
			array = array[0].split(' ')
			
			for i in range(0,len(array)):
				if array[i] == '':
					array.pop(i)
				
				else:
					array[i] = int(array[i])

			print "Enumeration:"
			milli_sec_start = int(round(time.time() * 1000))
			maxsub = enumeration(array)
			milli_sec_fim = int(round(time.time() * 1000))
			tempo = milli_sec_fim - milli_sec_start
			print "Tempo: " + str(tempo) + " ms"
			print "Max Subarray: " + str(maxsub) + "\n"

			# -------------------------------------------- Div and Conquer
			
			print "Div and Conquer:"
			milli_sec_start = int(round(time.time() * 1000))
			maxsub = Divide(array,0,len(array)-1)
			milli_sec_fim = int(round(time.time() * 1000))
			tempo = milli_sec_fim - milli_sec_start
			print "Tempo: " + str(tempo) + " ms"
			print "Max Subarray: " + str(maxsub) + "\n"
			

			# --------------------------------------------- Dynamic
			print "Dynamic:"
			milli_sec_start = int(round(time.time() * 1000))
			
			maxsub = dynamic(array)

			milli_sec_fim = int(round(time.time() * 1000))

			tempo = milli_sec_fim - milli_sec_start
			print "Tempo: " + str(tempo) + " ms"

			print "Max Subarray: " + str(maxsub) + "\n"
			# ---------------------------------------------			

	
	f.close()
	fw.close()

	return 0

if __name__ == '__main__':
	A = [0,1,2,3,4,5]
	gerarArray()

	
