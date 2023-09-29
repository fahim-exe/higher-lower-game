def get_a(index):
    temp = [0]*2
    a_set = {
    "name": ["Neymar", "Messi", "Ronaldo", "SRK", "Tom Cruse"],
    "salary": [2,5,4,30,20]
    }

    temp[0] = a_set["name"][index]
    temp[1] = a_set["salary"][index]

    return temp

    



def get_b(index):
    temp = [0]*2
    b_set = {
    "name":["Shakib", "Rock", "Jennifer lawrence", "Salman Khan", "Pele"],
    "salary": [1, 3, 6, 8, 15]
    }

    temp[0] = b_set["name"][index]
    temp[1] = b_set["salary"][index]

    return temp


def get_winner(a_sal, b_sal):
    if a_sal>b_sal:
        a = "a"

        return a

    if b_sal>a_sal:
        b = "b"
        return b


