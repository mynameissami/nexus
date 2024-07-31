import re
import json
from colorama import Fore, Back, Style

class Nexus():
    def __init__(self, user_name=None):
        self.user_name = user_name
        
    def json_load_resp(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    
        
    def get_advanced_response(self,user_input, responses):
        
        user_name = self.user_name
        # Check for specific keywords in the user input
        if re.search(r'\b(hello|hi)\b', user_input):
            return responses.get("hello", responses["default"])
        
        elif re.search(r'\b(tell\sme\sthe\smeaning|tell\sthe\smeaning|meaning\sof)\b', user_input):
            nexus = Nexus()
            nexus.dictionary_chat(nexus.chat)
            return None
        elif re.search(r'(?i)\b(tell\sme\sthe\sdate|tell\sthe\sdate|what\sis\sthe\sdate\stoday|what\sis\sthe\sdate)\b', user_input):
            nexus = Nexus()
            return nexus.date()

        elif re.search(r'\bhow\b.*\bare\b.*\byou\b', user_input):
            return responses.get("how are you", responses["default"])
        
        elif re.search(r'\bbye\b', user_input):
            return responses.get("bye", responses["default"])
       
        elif re.search(r'\bname\b', user_input):
            return responses.get("name", responses["default"])
        
        else:
            return responses["default"]
    def date(self):
        import datetime
        x = datetime.datetime.now()
        print(x.date())
    def dictionary_chat(self, user_name):
        
         def read_dictionary(self,file_path):
             with open(file_path, 'r') as file:
                return json.load(file)
            
           
         dictionary = read_dictionary(self, 'dictionary.json')  
         
         def get_meaning(self, word, dictionary):
            return dictionary.get(word.lower(), "I'm sorry, I don't know the meaning of that word.")
         
         def dic_chat(self, dictionary):
            print(f"{Fore.RED}NEXUS: Sure! What word would you like to know the meaning of?")
            while True:
                user_input = input(f"{Fore.BLUE}{fusrname}: ")
                if user_input == "back":
                    break
                # Extract the word from the user input
                words = re.findall(r'\b\w+\b', user_input)
                for word in words:
                    if word in dictionary:
                        meaning = get_meaning(self,word, dictionary)
                        print(f"{Fore.RED}NEXUS: The meaning of '{word}' is: {meaning}")
                        break
                else:
                    print("NEXUS: I'm sorry, I don't understand. Can you ask about a word's meaning?")
         dic_chat(self,dictionary)
    
    def chat(self,responses):
        if self.user_name is None:
            self.user_name = input(f"{Fore.BLUE}NEXUS: Enter your name: ")
            global fusrname
            fusrname = self.user_name

        while True:
            user_input = input(f"{Fore.BLUE}{self.user_name}: ")
            if user_input.lower() == "bye":
                print(f"{Fore.RED}NEXUS: {responses['bye']}")
                break
            response = Nexus.get_advanced_response(self,user_input, responses)
            if response is None:
                pass
            else:
                print(f"{Fore.RED}NEXUS: {response}")
if __name__ == "__main__":
    responses = Nexus.json_load_resp('responses.json')
    nexus = Nexus()
    nexus.chat(responses)

