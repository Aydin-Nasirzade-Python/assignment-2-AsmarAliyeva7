#import libraries here

def main():
  herf= input("Enter a letter of the alphabet: ")
  if herf=="a" or herf=="e" or herf=="i" or herf=="o" or herf=="u":
      print("Entered alphabet is a consonant!")
  elif herf=="y":
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
      print("Entered alphabet is a vowel!")
  pass

if __name__ == "__main__":
  main()
