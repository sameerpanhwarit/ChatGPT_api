import requests
import openai
import json
from time import sleep
import os
import sys

openai.api_key = 'your_api key here'
logo = "----------ChatGPT Python----------"
def main():
    os.system('cls')
    print(logo)
    menu=['1.Start ChatGPT',"2.Exit"]
    for i in menu:
        print(i)
    print('-'*20)
    opt = int(input("Choose Option: "))
    if opt == 1:
        chatGPT()
    elif opt == 2:
        pass
    else: 
        print("Invalid Option")
        sleep(0.5)
        os.system('cls')
        main()

def chatGPT():
    os.system('cls')
    print(logo)
    query = input("How may i help you? : ")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user",
            "content":query}]
    )
    data=response["choices"][0]["message"]['content']
    print("fetching data from server...")
    sleep(1)
    result(query,data)

def result(query,data):
    os.system('cls')
    print(logo)
    print("Question:",query)
    print(data)
    print("_"*27)
    option1 = input("Save response in file? y/n:")
    if option1== 'y' or 'Y':
        filename = input("Enter output filename: ")
        filename= filename+".txt"
        file = open(filename,'w')
        file.write(data)
        file.close()
        print("Save Data in File Successfully.")
    else:
        pass
    option2 = input("Go back to main menu? y/n:")
    if option2 == "y" or "Y":
        main()
    else:
        exit()
if __name__ == "__main__":
    main()
