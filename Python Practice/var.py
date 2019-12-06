class shop:
	biscuit = "50-50"#Class Variable
	def __init__(self):
		self.cho= "Dairymilk"# Instant Variable
		self.bill= 40
s1=shop()
s2=shop()
s1.cho="Kitkat"
shop.biscuit="Gooday"
print(s1.bill,s1.cho,s1.biscuit)
print(s2.bill,s2.cho,s2.biscuit)

