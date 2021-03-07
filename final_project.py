import smtplib

sender_email = ""
rec_email = ""
password = input(str('masukkan password: '))
message = "haloooooo"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been send to ", rec_email)

#referensi dari https://www.youtube.com/watch?v=sXjpkcF7rPQ
