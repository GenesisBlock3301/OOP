class Calculator:
	def __init__(self,a,b):
		self.a=a
    	        self.b=b
	def addition(self):
		print(self.a+self.b)
	def sub(self):
		print(self.a-self.b)
	def mul(self):
    	        print(self.a*self.b)
	def div(self):
    	        print(float(self.a/self.b))
print("Enter choice: ")
n=int(input())
if n==1:
	c=Calculator(int(input("Enter a: ")),int(input("Enter b: ")))
	c.addition()
elif n==2:
	c=Calculator(int(input("Enter a: ")),int(input("Enter b: ")))
	c.sub()
elif n==3:
	c=Calculator(int(input("Enter a: ")),int(input("Enter b: ")))
	c.mul()
elif n==4:
	try:
		c=Calculator(int(input("Enter a: ")),int(input("Enter b: ")))
    	        c.div()
	except:
		print("Divided by Zero")
else:
	print("Operation not possible")
