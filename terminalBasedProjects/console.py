information = []
askHobbiesList = []


t = [1,2,3,4,5,6,7,8,9,10]


askName = input("What is your name? ")
askLikes = input("What do you like to do? ")
askAge = input('How old are you ?')
askHobby = int(input('How many hobbies do you have?'))

def hobby(askHobby):
    if askHobby >= 1:
        print('You have ' + str(askHobby) + ' hobbies')
    if askHobby >= 1:
        while askHobby >= 1:
            askMoreHobbies = input('What is one of your hobbies?')
            askHobbiesList.append(askMoreHobbies)
            askHobby = askHobby - 1
            print(askMoreHobbies)
            if askHobby == 0:
                print('Your hobbies are:')
                for i in askHobbiesList:
                    print(i)
                    if i == 'Soccer':
                        print('You are a soccer fan')
                        x = askHobbiesList.find('Soccer')
                        print(x)
                        
                break

    


def addList(askName, askLikes, askAge):
    information.append(askName)
    information.append(askLikes)
    information.append(askAge)
    return information


hobby(askHobby)
addList(askName, askLikes, askAge)
