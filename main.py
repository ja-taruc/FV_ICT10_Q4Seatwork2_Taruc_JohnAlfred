from pyscript import document

# A simple list to save our sentences
classmate_list = []

def add_student(event):
    # 1. Grab what the user typed
    name = document.querySelector("#name-in").value
    section = document.querySelector("#section-in").value
    subject = document.querySelector("#subject-in").value

    # 2. Combine them into one sentence
    sentence = f"Hi! I am {name} from {section}. My favorite subject is {subject}."

    # 3. Add that sentence to our list
    classmate_list.append(sentence)

    # 4. Clear the boxes for the next person
    document.querySelector("#name-in").value = ""
    document.querySelector("#section-in").value = ""
    document.querySelector("#subject-in").value = ""
    
    document.querySelector("#display-area").innerText = "Added!"

def display_list(event):
    # Find the output box
    box = document.querySelector("#display-area")
    
    # Clear the box first
    box.innerHTML = ""

    # Loop through the list and show each sentence
    for person in classmate_list:
        # Create a new paragraph tag for each person
        new_text = document.createElement("p")
        new_text.innerText = person
        # Put the paragraph inside the box
        box.appendChild(new_text)