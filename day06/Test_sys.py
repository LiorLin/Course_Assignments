import sys

def ncbi_search():
  print(sys.argv) 

  if len(sys.argv) < 3:
    print("Please provide at least three arguments.")
    
  else:
    term = sys.argv[1]
    num = sys.argv[2]
    return term, num
   


