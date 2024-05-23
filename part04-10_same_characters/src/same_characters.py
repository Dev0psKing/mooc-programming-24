# Write your solution here
def same_chars(a,b,c):
   a,b,c = str(a), int(b), int(c) 
   if b < 0 or c < 0 or b >= len(a) or c >= len(a):
        return False
   else:
      return  a[b] == a[c]
       
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))