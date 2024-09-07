import smtplib
import os


def send_mail(body_no, stu_mail, subject_):
    MAIL_ID = os.environ.get('LODESTAR_MAIL')
    PASSWORD = os.environ.get('LODESTAR_PASS')
    prof_msg = f"Subject: Student attendance report\n\nThe following student has lack of attendance in your subject: {stu_mail[0]}"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(MAIL_ID, PASSWORD)

        subject = 'Attendance report'
        if body_no == 1:
            body = f"Warning!! You can take only one more day leave for {subject_} class"
        elif body_no == 2:
            body = f"You have lack of attendance in {subject_}"
            smtp.sendmail(MAIL_ID, MAIL_ID, prof_msg)
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(MAIL_ID, stu_mail[1], msg)
