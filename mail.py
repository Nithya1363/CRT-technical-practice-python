msg = input("Invitation Msg: ")
emails = [
    'john.deer@gmail.com',
    'alex.barner@yahoo.com',
    'brad.cooper@hotmail.com',
    'cindy.barner@hotmail.com',
    'matt.damon@gmail.com',
    'george.cloony@yahoo.com',
    'mc.barner@hotmail.com'
]
def send_invitation(mail:str, msg:str):
    print(f"Invitaion {msg} sent to {mail}")

for mail in emails:
    ind = mail.find("@")
    if mail[ind:] != "@hotmail.com":
        send_invitation(mail, msg)