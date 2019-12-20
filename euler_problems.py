import math

#my approach at euler problems

#Problem 1 - Multiples of 3 and 5

def problem1():
	sum53 = 0

	i = 1
	for i in range(1000):
		if i % 3 ==0:
			sum53 = sum53 + i
		if i % 5 ==0:
			sum53 = sum53 + i	
		if i % 3 == 0 and i % 5 == 0:
			sum53 = sum53 - i	
	
	return sum53

#problem 2 - Even Fibonacci numbers	Even Fibonacci numbers

def problem2():
	sumFibs = 0
	thresh = 4000000
	fibMin1 = 1
	fibMin2 = 1
	fibNum = 2
	while(1):
		if fibNum > 4000000:
			break
		fibNum = fibMin1 + fibMin2
		if fibNum % 2 ==0:
			fibMin2 = fibMin1
			fibMin1 = fibNum
			sumFibs = sumFibs+fibNum
		else: 
			fibMin2 = fibMin1
			fibMin1 = fibNum
	return sumFibs		

#problem 3 - Largest prime factor

def problem3():
	largeNum = 600851475143
	thresh = 600851475143
	primeFac = []
	factor = 2
	while(thresh>1):
		if largeNum % factor == 0:
			primeFac.append(factor)
			factor +=1
			thresh = thresh/factor
		else:
			factor+=1
	return max(primeFac)			

#problem 4 - Largest palindrome product

def problem4():
	sixDigNum = 999999
	biggestPalin = 999999
	while(1):
		if checkIfPalin(sixDigNum):
			isValid = hasTwoThrDigNums(sixDigNum)			
			if isValid:
				biggestPalin = sixDigNum
				break
			sixDigNum-=1
		sixDigNum-=1
	
	return biggestPalin
	
	
def hasTwoThrDigNums(num):
	prodOfThrDig = False
	number = num
	factor1 = 999
	factor2 = 999
	while(factor1>100):
		if number%factor1 == 0:
			factor2 = number/factor1
			if factor2<1000:
				prodOfThrDig = True
			factor1-=1
		factor1-=1	
	return prodOfThrDig 
	
			
def checkIfPalin(product):
	isPalin = True
	lengthNum = len(str(product))
	numList = []
	for i in range(lengthNum):
		numList.append(int(product % 10))
		product = product/10
	isEven = True
	if len(numList)%2 == 0:
		isEven = True
	else:
		isEven = False
	if isEven:
		for i in range(int(len(numList)/2)):

			if numList[i] != numList[-i-1]:
				isPalin = False
	else:
		for i in range((len(numList)-1)/2):
			if numList[i] != numList[-i+1]:
				isPalin = False							
	return isPalin	
	
#problem 5 - 	Smallest multiple
	
def problem5():
	numbersToDiv = [20,19,18,17,16,15,14,13,12,11]
	divider = 20
	number = 20
	finalNum = 1
	while(1):
		if divider == 1:
			finalNum = number
			break
		else:
			divider-=1
			if number%divider != 0:
				number+=20
				divider = 20
	return finalNum				
		
#problem 6 - sum square difference
		
def problem6():	
	sumSquareList = []
	squaredSumList = []
	listOneHun = []
	for i in range(101):
		sumSquareList.append(i**2)
	sumSquares = sum(sumSquareList)
	for i in range(101):
		squaredSumList.append(i)
	squaredSum = sum(squaredSumList)**2
	diff = squaredSum - sumSquares		
	return diff
							
def main():
	print("Awnser to Problem1 is " + str(problem1()))
	print("Awnser to Problem2 is " + str(problem2()))
	print("Awnser to Problem3 is " + str(problem3()))
	print("Awnser to Problem4 is " + str(problem4()))
	print("Awnser to Problem5 is " + str(problem5()))
	print("Awnser to Problem6 is " + str(problem6()))

if __name__ == '__main__':
    main()
