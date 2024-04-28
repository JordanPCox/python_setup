def hello():
    print("Greetings, Earthling!")

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]
result = pack("wallet", "phone", "keys")
print(result)

def eat_lunch(lunchbox_contents):
    if lunchbox_contents:
        print(f"I'm going to eat {lunchbox_contents[0]}")
        for item in lunchbox_contents[1:]:
            print(f"Next I eat {item}")
    else:
        print("I sure am hungry!")

eat_lunch(["apple", "banana", "carrot"])