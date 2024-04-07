#import libraries here

def main():
  x=float(input("Enter x: "))
  y=float(input("Enter y: "))
  if (x>=0 and y>=0 and y>=(x-2)**2-3 and x>=abs(y)) or (x>=0 and y<=0 and y>=(x-2)**2-3 and x<=abs(y)):
      print("The point is in the shaded area")
  else:
      print("The point is not in the shaded area")
 
  pass

if __name__ == "__main__":
  main()
