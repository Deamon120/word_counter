while True:
    text = input("Write a text: ")
    if not text.strip():
            print("Empty text, try again!")
            continue

    text_split = text.split()

    counter = 0
    for word in text_split:
        counter += 1

    print(f"Number of words in text: {counter}")
    while True:
        choice = input("Continue with new text? (yes/no)").lower()
        if choice == "yes":
            break
        elif choice == "no":
             print("End of the program. Bye!")
             exit()
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
            continue
        
        

