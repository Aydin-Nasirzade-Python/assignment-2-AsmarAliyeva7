#import libraries here

def main():
  w=int(input("Enter the wavelength in nm: "))
  if w>=380 and w<450:
      print("The relevant color is Violent")
  elif w>=450 and w<495:
      print("The relevant color is Blue")
  elif w>=495 and w<570:
      print("The relevant color is Green")
  elif w>=570 and w<590:
      print("The relevant color is Yellow")
  elif w>=590 and w<620:
      print("The relevant color is Orange")
  elif w>=620 and w<750:
      print("The relevant color is Red")
  else:
      print("Invalid input!")
  
  
  pass

if __name__ == "__main__":
  main()
