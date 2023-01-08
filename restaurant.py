# This is a modified version of the code found here: https://repl.it/@lagrassom/chatbot01

import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses


def generate_response(user_input):
  responses = [
    "I'm not sure...", "I don't know.", "They tell me nothing.", "IDK.",
    "I'll let you know when I find out.", "Good question!"
  ]
  if "order" in user_input.split(" "):
    return "I'll get that right out for you."
  elif "menu" in user_input.split(" "):
    return "We have every type of pasta."
  elif ("special" in user_input.split(" ")) or ("specials" in user_input.split(" ")):
    return "Our special of the day is the special pasta."
  elif ("reserve" in user_input.split(" ")) or ("reservation" in user_input.split(" ")):
    return "I'll put in your reservation."
  return random.choice(responses)


def init_chat():
  quit_characters = ['q', "thanks", "thx", "thank you", "ty", "no"]
  user_input = input("Hello, this is a resturant. How can I help you?\n")

  while user_input not in quit_characters:
    #Ask the user for more input, then use that in your response
    user_input = input(
      generate_response(user_input) +
      " Is there anything else I can do for you?\n")

  print("Glad I could be of service.")


if __name__ == "__main__":
  init_chat()
