#-*- coding utf-8 -*-

def create_record(name, phone, adress):
    """create_record"""
    record = {
        "name": name,
        "phone": phone,
        "adress": adress
    }
    return record


user1 = create_record("Vanya", '+7898989898', "Tunis")
user2 = create_record("Petya", "+7989898776", "Moroko")


print(user1)
print(user2)