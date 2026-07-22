#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments

def make_shirt(size, message):
    print(f"the size of the shurt is {size}, and the text printed on it is {message.title()}")

make_shirt("24","bytesbyaman")
make_shirt(size='24',message="aman")
