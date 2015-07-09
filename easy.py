def FirstReverse(str): 
  return str[::-1]


def FirstFactorial(num): 
  k = 1
  for i in range(1, num+1):
    k *= i
  return k  



def LongestWord(string): 
#"a beautiful sentence^&!"
#"letter after letter!!" 
# "a confusing /:sentence:/[ this is not!!!!!!!~" 

  for char in string:
  	#char.isalpha():
  	if char in " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
  		continue
  	else:
  		string.replace(char, "")
  
  return max( list(string.split(' ')), key=len )

print(LetterChanges("a beautiful sentence^&!"))


def LetterChanges(instr): 
  out = "" 
  for char in instr:
    if char.isalpha():
      ch = chr(ord('a') + (ord(char) + 1 - ord('a')) % 26)
    else:
    	ch = char
    if ch in 'aeiou':
      ch = ch.upper()
    out += ch
  return out
    

def SimpleAdding(num): 
  out = 0 
  for i in range(num+1):
    out += i
  return out 



def LetterCapitalize(str):
  out = ""
  lst = list(str)
  for word in lst:
    out += word.capitalize() 
    
  return out 


  def LetterCapitalize(str):
  lst = list(str.split(' '))
  for word in lst:
    str = str.replace(word, word.capitalize()) 
  return str 

  

