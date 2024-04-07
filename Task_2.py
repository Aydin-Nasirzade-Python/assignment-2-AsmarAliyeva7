#import libraries here

def main():
  month=input("Enter name of the month [ex. June]: ")
  day=input("Enter the day [ex. 5]: ")
  a="AprilMay"
  b="JulyAugust"
  c="NovemberOctober"
  if month=="March" and day>=20 or month=="June" and day<21 or month in a:
      print(f"{month} {day} is in Spring")
  elif month=="June" and day>=21 or month=="September" and day<22 or month in b:
      print(f"{month} {day} is in Summer")
  elif month=="September" and day>=22 or month=="December" and day<21 or month in c:
      print(f"{month} {day} is in Fall")
  else:
      print(f"{month} {day} is in Winter")
  
  pass

if __name__ == "__main__":
  main()
