# This is a modified version of the code found here: https://repl.it/@lagrassom/chatbot01

import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "That's Great!",
    "Tell me more!",
    "Oh Wow!",
    "That's crazy!"
  ]
  return random.choice(responses)

def init_chat():
  quit_characters = [
      'q',
      "Bye",
      "bye",
      "I gtg",
      "igtg",
      "gtg",
      "cya",
      "stop",
      "Stop",
      "STOP"
      "I have to go",
      "I got to go"
  ]
  user_input = input("Hello, how are you?\n")

  while user_input not in quit_characters:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

  print("Bye!")

if __name__ == "__main__":
  init_chat()