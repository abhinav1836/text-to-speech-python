import os
import pyttsx3   #imported externally

if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.say("Is it working")
    engine.runAndWait()

# if __name__ == "__main__":
#     com=f"Say hello"
#     os.system(com)  #WORKS IN LINUX OS