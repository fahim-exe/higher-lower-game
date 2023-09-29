import random as R
import game as G

score = 0
while True:

    a = G.get_a(R.randint(0,4))
    b = G.get_b(R.randint(0,4))

    print(f"Compare A: {a[0]}")
    print()
    print(f"Against B: {b[0]}")
    winner = G.get_winner(a_sal=a[1], b_sal=b[1])

    user_input = input("Who has more salary? Type 'A' or 'B': ").lower()

    if user_input==winner:
        score+=1
        print()
        print(f"You are right! Current Score: {score}.")

    else:
        print()
        print(f"Sorry, that's wrong. Final Score: {score}")
        break
    

