di = {}
uniq_id = 1

def create_note():
    global uniq_id
    text = input("Enter your  note:  ")
    di[uniq_id] = text
    print(f"Note ID:  {uniq_id}")
    uniq_id += 1

def list_notes():
    if not di:
        print("No notes available.")
    else:
        for id, text in di.items():
            print(f"ID: {id}, PNote: {text[:30]}")

def retrieve_note():
    id = int(input("Enter note ID: "))
    if id in di:
        print(f"Note : {di[id]}")
    else:
        print("Note not found.")

def delete_note():
    id = int(input("Enter note ID for deleteing:  "))
    if id in di:
        del di[id]
        print("Note deleted.")
    else:
        print("Note not found.")

def search_notes():
    inp = input("Enter note to search: ")
    found = False
    for id, text in di.items():
        if inp.lower() in text.lower():
            print(f"ID: {id}, Note: {text}")
            found = True
    if not found:
        print("Note  not found:")


def note_menu():
    while True:
        print()
        print("Note Taking App")
        print("1. Create Note")
        print("2. List Notes")
        print("3. Retrieve Note")
        print("4. Delete Note")
        print("5. Search Notes")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "6":
            print("Good bye")
            break
        if choice in ('1', '2', '3', '4', '5'):
            new_di = {"1": create_note, "2": list_notes, "3": retrieve_note, "4": delete_note, "5": search_notes}
            res = new_di[choice]()
        else:
            print('Please enter a number between 0 and 5.\n')
note_menu()
