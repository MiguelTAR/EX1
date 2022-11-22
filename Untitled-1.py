#New code at beginning of file #wcober
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

def display_output(ourchicken, myfizzbuzz):
  if (ourchicken):
    ourchicken = 'Big fat chicken'
  else:
    ourchicken = ''
  if (myfizzbuzz == 'f'):
    myfizzbuzz = "I have the fizz"
  if (myfizzbuzz == "b"):
    myfizzbuzz = 'I have the buzz'
  if (myfizzbuzz == 'fb'):
    myfizzbuzz = 'I really like the fizz and the buzz'
    
  buzzandchicken = '' 
  if (ourchicken and myfizzbuzz) :
   buzzandchicken = ", and"
     
    
    
  print("{}: {}{} ".format(str(value), myfizzbuzz, buzzandchicken, ourchicken))
  
       
for valuex in range(1,16):
  myfizzbuzzx = fizzbuzz(valuex)
  mychickenz = chicken(valuex)
  #print("{}: {} {} ".format(str(value), myfizzbuzz, mychicken))
  display_output(mychickenz, myfizzbuzzx)


  # Checked the code / all clear #wcober
  # - FIzzBUZZZ

