# Student Club Member Checker
from pyscript import display, document


def student_club(e):
    document.getElementById('result').innerHTML = ' '
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    studentname = firstname + ' ' + lastname
    ss_members = ['Gurleen Kaur', 'Savannah Reyes', 'Katalina Pingol', 'Helena Magsino', 'Zoe Bueno', 'Simran Kaur']
    member_checker = studentname in ss_members

    display_message = (f'Sorry {studentname}, your name is not on the list.', f'Congratulations {studentname}, you are now part of the Social Studies Club!')

    document.getElementById('result').innerHTML = (display_message[member_checker])
    