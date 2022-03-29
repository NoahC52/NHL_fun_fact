# imported modules
import random
# Dictionary for the current teams I have selected.
nhl_dict = {
    "toronto": "Toronto Maple Leafs",
    "boston": "Boston Bruins",
    "montreal": "Montreal Canadiens",
    "new york": "New York Rangers",
    "detroit": "Detroit Red Wings",
    "chicago": "Chicago Blackhawks",
    "glendale": "Arizona Coyotes",
}
# Fun fact list of the various teams I have selected.
fun_fact_toronto = ["They have won a total of 13 Stanley Cups.", "They were founded in 1917."]
fun_fact_boston = ["Were one of the original 6 teams of the NHL.", "They were the first american team to join the NHL"]
fun_fact_montreal = ["They have a record number of Stanley Cups at 24!", "They were founded in 1909."]
fun_fact_new_york = ["The Rangers have never had a mascot.", "They were founded in 1926."]
fun_fact_detroit = ["The Red Wings were one of the first 6 NHL teams.", "They have won a total of 11 stanley cups."]
fun_fact_chicago = ["Blackhawks used to be two words until 1986.", "The Rockford ice hogs are affiliated with them."]
fun_fact_glendale = ["Mika Alatalo played with Finland in the 1994 Olympics.", "The jersey #9 was un-retired in 2005."]
# Global variables
count = 0
user_response = []


# Begin the While Loop.
def team_input():
    while count == 0:
        # Finding out what team the user wants.
        user = input("\nWhat's the location of the NHL team would you like to view?: ").lower()
        # Begin checking to see if said team is in the current dictionary.
        if user in nhl_dict:
            print("\nThe location of that team is:", user.title(), "and the team name is:", nhl_dict[user])
            user_response.append(user)
            break
        # Not in dictionary, so we go back.
        if user not in nhl_dict:
            print("\nSorry I didn't understand that. Let's try that again!")


team_input()
# Begin of checking if the user wants to know a fun fact.
fun_user = input("\nWould you like to know a fun fact?: (y) (n) ").lower()
if fun_user == "y" or fun_user == "yes":
    if user_response[0] == "toronto":
        print("\nHere is a fun fact about the Toronto Maple Leafs!:", random.choice(fun_fact_toronto))
    elif user_response[0] == "boston":
        print("\nHere is a fun fact about the Boston Bruins!:", random.choice(fun_fact_boston))
    elif user_response[0] == "montreal":
        print("\nHere is a fun fact about the Montreal Canadiens!:", random.choice(fun_fact_montreal))
    elif user_response[0] == "new york":
        print("\nHere is a fun fact about the New York Rangers!:", random.choice(fun_fact_new_york))
    elif user_response[0] == "detroit":
        print("\nHere is a fun fact about the Detroit Red Wings!:", random.choice(fun_fact_detroit))
    elif user_response[0] == "chicago":
        print("\nHere is a fun fact about the Chicago Blackhawks!:", random.choice(fun_fact_chicago))
    elif user_response[0] == "glendale":
        print("\nHere is a fun fact about the Arizona Coyotes!:", random.choice(fun_fact_glendale))
# Since we know now that the only option left is no, we just thank the user for testing and end it!
else:
    print("\nOkay, thank you for testing!")
