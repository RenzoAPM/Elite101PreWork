# This is a modified version of the code found here: https://repl.it/@lagrassom/chatbot01

import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses


def generate_response(user_input):
  responses = [
    "I'm not sure...", "I don't know.", "They tell me nothing.", "IDK.",
    "I'll let you know when I find out.", "Good question!"
  ]
  if "balance" in user_input.split(" "):
    return "You have $10 in your checkings acount, and $11 in your savings account."
  elif ("move" in user_input.split(" ")) or ("transfer" in user_input.split(" ")):
    return "I put in a transfer request."
  elif ("sell" in user_input.split(" ")) or ("products" in user_input.split(" ")):
    return "We have a new credit card you can buy. We also have accountants available for service."
  elif "service" in user_input.split(" "):
    return "We have accountants available for service."
  return random.choice(responses)


def init_chat():
  quit_characters = ['q', "thanks", "thx", "thank you", "ty", "no"]
  user_input = input("Hello, this is a financial institution. How can I help you?\n")

  while user_input not in quit_characters:
    #Ask the user for more input, then use that in your response
    user_input = input(
      generate_response(user_input) +
      " Is there anything else I can do for you?\n")

  print("Glad I could help.")


if __name__ == "__main__":
  init_chat()
