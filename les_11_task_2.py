def hide_email(mail: str):
    mail_name = mail.split('@')[0]
    hosting_name = mail.split('@')[1]
    return mail_name[:2] + '*' * (len(mail_name) - 2) + '@' + '*' * (len(hosting_name) - 4) + hosting_name[-4:]


print(hide_email('somebody_email@gmail.com'))
