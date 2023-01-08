# This is a modified version of the code found here: https://repl.it/@lagrassom/chatbot01

import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses


def generate_response(user_input):
  responses = [
    "I'm not sure...", "I don't know.", "They tell me nothing.", "IDK.",
    "I'll let you know when I find out.", "Good question!"
  ]
  if ("when" in user_input.split(" ")) or ("hours" in user_input.split(" ")):
    return "Our hours are 9:00 AM to 5:00 PM on Mondays through Saturdays. We are closed on Sundays."
  elif "where" in user_input.split(" "):
    return "We are located at Slaughter Ln and Real St."
  elif ("have" in user_input.split(" ")) or ("sell" in user_input.split(" ")):
    return "We only sell sailboat fuel"
  elif ("cost" in user_input.split(" ")) or ("price" in user_input.split(" ")):
    return "We sell sailboat fuel for FREE!"
  return random.choice(responses)


def init_chat():
  quit_characters = ['q', "thanks", "thx", "thank you", "ty", "no"]
  user_input = input("Hello, this is costumer service. How can I help you?\n")

  while user_input not in quit_characters:
    #Ask the user for more input, then use that in your response
    user_input = input(
      generate_response(user_input) +
      " Is there anything else I can help you with?\n")

  print("Glad I could help!")


if __name__ == "__main__":
  init_chat()
