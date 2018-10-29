from game import *
from tools import is_waiting
from data import again_response_list

while True:
    new_game()
    
    Response = ""
    while is_waiting(Response, again_response_list) is False:
        Response = input("Again (Y/N)? : ")
        if Response!="N" and Response!="Y":
            print("ERROR ! Waiting 'Y' or 'N' !")

    if Response=="N":
        break