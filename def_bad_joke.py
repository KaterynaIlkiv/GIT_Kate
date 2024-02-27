import sys

def bad_joke_year(year):
    print('How old are you?')
    year=int(sys.stdin.readline())
    if year>=10 and year<=13:
      print('Count the years.How many will be 13+49+84+155+97? Too much')
    else:
        print('What?')  
        
bad_joke_year(7) 