def main():
  print("Welcome to my math quiz!")
  print("<----Main Menu---->")
  print("(A) Settings")
  print("(B) Difficulty")
  print("(C) Leaderboard")

#options for the students to choose
  choice = input("Please select one of the options:")

#do something what use says (Main menu)
  
  if choice == "a":
    pass
  elif choice =="b":
    difficulty()
  else:
    main()
    
#difficulty level
def difficulty():
  print("Choose your difficulty")
  print("(a) Easy")
  print("(b) Medium")
  print("(c) Hard")




 
main()
