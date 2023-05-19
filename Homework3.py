
# QUESTION 1: Jumping The Queue

from collections import deque


def process_queue(input_file):
    queue = deque()

    with open(input_file, 'r') as file:
        for line in file:
            action, name = line.strip().split()
            if action == 'JUMP':
                queue.appendleft(name)
            elif action == 'JOIN':
                queue.append(name)

    return list(queue)


input_file = 'hom3.txt'
final_order = process_queue(input_file)
print(final_order)


"""based on the value of action, the code performs different operations on the queue.
If action is equal to 'JUMP', it means the person named name is skipping ahead in the queue.
    In this case, name is appended to the left end of the queue using the appendleft() method of the deque object. 
If action is equal to 'JOIN', it means the person named name is joining the queue. In this case, name is appended to the right end 
of the queue using the append() method of the deque object""""""





# QUESTION 2: Number In Sequence

def num_in_seq(n):
    first_number = 8
    common_difference = 7

    nth_number = first_number + (n - 1) * common_difference

    return nth_number
print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))

# the function takes an input n representing the position of the number in the sequence. It first checks if the 
# input is a positive integer. If the input is less than 1, it returns an error message indicating an invalid input






# QUESTION 3: Hyperlink History

base_url = "https://codefirstgirls.com"
category_urls = ["/courses", "/opportunities"]
subcategory_urls = ["/courses/cfgdegree", "/opportunities/ambassadors"]

current_url = base_url

while True:
    print("You are currently on the URL", current_url)
    print("Where are you clicking?")
    print("Options:", end=" ")

    if current_url == base_url:
        print("Courses, Opportunities")
    elif current_url in category_urls:
        print("CFGDegree, Back")
    elif current_url in subcategory_urls:
        print("Back")

    choice = input()

    if choice.lower() == "courses":
        current_url = base_url + "/courses"
    elif choice.lower() == "opportunities":
        current_url = base_url + "/opportunities"
    elif choice.lower() == "cfgdegree" and current_url in category_urls:
        current_url = base_url + "/courses/cfgdegree"
    elif choice.lower() == "back":
        if current_url in category_urls:
            current_url = base_url
        elif current_url in subcategory_urls:
            current_url = base_url + current_url.split('/')[1]

    print()


