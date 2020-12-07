# for loop

for letter in "Giraffe Academy":
    print(letter)

friends = ["Kevin", "Jim", "Pam"]

for friend in friends:
    print(friend)

for index in range(3,10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")