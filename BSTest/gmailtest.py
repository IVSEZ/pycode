import imaplib
import email
import getpass

# p = getpass.getpass()

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('username', 'gmail pass')

# print(mail.list())

mail.select('INBOX')

# result, data = mail.uid('search', None, "BODY \"Meter Readings\"")
# result, data = mail.uid('search', None, "ALL")
result, data = mail.uid('search', None, '(OR (TO "philip@paphitis.co.za") (TO "philip.johnpap@gmail.com"))')
i = len(data[0].split())  # data[0] is a space separate string
for x in range(i):
    latest_email_uid = data[0].split()[x]  # unique ids wrt label selected
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # fetch the email body (RFC822) for the given ID
    raw_email = email_data[0][1]
    # print(raw_email)
    email_message = email.message_from_bytes(raw_email)
    # print(email_message)
    to_email = email_message['To']
    # if(to_email == 'philip.johnpap@gmail.com'):
    print(email_message['To'] + ' === ' + email_message['Date'])
    # print(email_message['Body'])


    #continue inside the same for loop as above
    raw_email_string = raw_email.decode('utf-8')
    # converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
    # this will loop through all the available multiparts in mail
    for part in email_message.walk():
        if part.get_content_type() == "text/plain": # ignore attachments/html
            body = part.get_payload(decode=True)
            reading = str(body).find("Electricity")
            print(str(reading))
            # save_string = str("D:Dumpgmailemail_" + str(x) + ".eml")
            save_string = "C:\\_out\\email_" + str(x) + ".txt"

            myfile = open(save_string, 'a')

            # myfile.write(str(body))
            # myfile.write(str(reading))
            # location on disk
            # myfile.write(body.decode('utf-8'))
            # body is again a byte literal
            myfile.close()
        else:
            continue