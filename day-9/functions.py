users = []

def new_player(name, bid):
    user = {}
    user["name"] = name
    user["bid"] = bid
    users.append(user)

def find_max(list):
    highest_bidder = {}
    max_ = 0
    for dictionary in list:
        value = dictionary["bid"]
        if value > max_:
            max_ = value
            highest_bidder = dictionary
    
    return highest_bidder