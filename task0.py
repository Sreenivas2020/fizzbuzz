

def fizzbuzz(maximum_num=101):
    for i in range(maximum_num):
        value = ""
        if i % 3 == 0: value += "Fizz"
        if i % 5 == 0: value += "Buzz"
        yield value if value else i

for number, burp in enumerate(fizzbuzz()):
	print ("%s: %s" % (number, burp))
