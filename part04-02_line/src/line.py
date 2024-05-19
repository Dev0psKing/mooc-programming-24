# Write your solution here
# You can test your function by calling it within the following block
def line(integer, string):

    if string == "":
        print(integer * "*")
        
    else:
     print(integer * string[0])

    
if __name__ == "__main__":
    line(5, "LOL")