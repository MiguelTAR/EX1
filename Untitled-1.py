def chicken(value):
  chicken = 0
  if (value % 10 == 0):
        chicken = 1

  return chicken

def fizzbuzz(value):
    fizzbuzz = ''
    if(value % 5 == 0 and value % 3 == 0):
        fizzbuzz = 'fb'
    
    if(value % 3 == 0):
      fizzbuzz = 'f'
        

    if(value % 5 == 0):
      fizzbuzz = "b"
    return fizzbuzz

def display_output(mychicken, myfizzbuzz):
  if (mychicken):
    mychicken = 'Big fat chicken'
  else:
    mychicken = ''
  if (myfizzbuzz == 'f'):
    myfizzbuzz = "I have the fizz"
  if (myfizzbuzz == "b"):
    myfizzbuzz = 'I have the buzz'
  if (myfizzbuzz == 'fb'):
    myfizzbuzz = 'I really like the fizz and the buzz'
    
  buzzandchicken = '' 
  if (mychicken and myfizzbuzz) :
   buzzandchicken = ", and"
     
    
    
  print("{}: {}{} ".format(str(value), myfizzbuzz, buzzandchicken, mychicken))
  
       
for value in range(1,16):
  myfizzbuzz = fizzbuzz(value)
  mychicken = chicken(value)
  #print("{}: {} {} ".format(str(value), myfizzbuzz, mychicken))
  display_output(mychicken, myfizzbuzz)

