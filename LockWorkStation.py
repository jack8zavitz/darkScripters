import email, imaplib,ctypes

def lock():
    user32 = ctypes.cdll.LoadLibrary("user32.dll") 
    user32.LockWorkStation()
    return
    
def checkMail():
    user = "your_email"
    pwd = "email_password"

    # connecting to the gmail imap server
    m = imaplib.IMAP4_SSL("imap.gmail.com")
    m.login(user,pwd)
##    m.list()
    m.select("INBOX") # here you a can choose a mail box like INBOX instead
    # use m.list() to get all the mailboxes1
    resp, items = m.search(None, "UNSEEN") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
    items = items[0].split() # getting the mails id

    for emailid in items:
        resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        email_body = data[0][1] # getting the mail content
        mail = email.message_from_string(email_body) # parsing the mail content to get a mail object    

        if mail["Subject"]=="Lock":
            lock()

        
    m.close() # close the mailbox
    m.logout()# logout

while True:
    checkMail()
    
