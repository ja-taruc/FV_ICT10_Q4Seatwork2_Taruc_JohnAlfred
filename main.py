from pyscript import document

classmate_list = []

def add_student(event):
    # To get what the user inputs
    name = document.querySelector("#name-in").value
    section = document.querySelector("#section-in").value
    subject = document.querySelector("#subject-in").value

    # From the inputs, it formats it to a sentence
    sentence = f"Hi! I am {name} from {section}. My favorite subject is {subject}."

    
    classmate_list.append(sentence)

  
    document.querySelector("#name-in").value = ""
    document.querySelector("#section-in").value = ""
    document.querySelector("#subject-in").value = ""
    
    document.querySelector("#display-area").innerText = "Added!"

def display_list(event):
  
    box = document.querySelector("#display-area")
    

    box.innerHTML = ""

    
    for person in classmate_list:
       
        new_text = document.createElement("p")
        new_text.innerText = person
        box.appendChild(new_text)
