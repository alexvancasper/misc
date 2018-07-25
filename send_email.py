#!/usr/bin/python
import paramiko
import socket,sys, smtplib
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders

fromaddr = "????????????@rambler.ru"
toaddr = "receipent address"
mypass = "PASSWORD"

se='192.168.0.1'
username='admin'
password='admin'
cmd="show memory"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(se, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
s=ssh_stdout.read();
ssh.close()
mem = s.split(",");
Total = mem[0].split(" "); Total = Total[2][:-1];
Used = mem[1].split(" "); Used = Used[2][:-1];
Free = mem[2].split(" "); Free = Free[2][:-1];

if Total.isdigit() and Used.isdigit() and Free.isdigit():
    Total=int(Total)
    Used=int(Used)
    Free=int(Free)
    UsedPercent = (Used * 100) / Total;
    FreePercent = (Free * 100) / Total;
    SMS = "Using memory:" + str(UsedPercent)+"%\n";
    SMS += "Free memory: "+str(FreePercent)+"%\n";
    SMS += s;
    print SMS;

if FreePercent<85:
#    print "Need reboot!!!";
    SMS += "Need reboot!!!"
else:
#    print "It's good. You can continue sleep "
    SMS += "it's good, yet!"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Percent of usage memory"
 
body = SMS
msg.attach(MIMEText(body, 'plain', 'utf-8'))
server = SMTP_SSL()
try:
    server.connect('smtp.rambler.ru', 465)
    server.ehlo()
    try:
	server.login(fromaddr,mypass)
    except smtplib.SMTPException, e:
	print "Authentication failed:", e
	sys.exit();
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print " *** your message may not have been sent! "
    print e
    sys.exit(2)
else:
    print "Message successfully sent "
#server.starttls()
#server.ehlo()

server.quit()
