import socket, string, time, math, base64
SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = 'Ck4aM-bot1'
CHANNEL = '#root-me_challenge'


def main():
    global IRC
    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IRC.connect((SERVER, PORT))
    Listener()
    IRC.close()


def send_data(command):
    IRC.send(bytes(command + '\n', 'UTF-8'))


def joinchan(chan):
    send_data('JOIN ' + chan)
    ircmsg = ""
    while ircmsg.find("is now your displayed host") == -1:
        ircmsg = IRC.recv(2048).decode("UTF-8")
        # DEBUG # print(ircmsg)


def Listener():
    send_data("USER " + NICKNAME + " " + NICKNAME + " " + NICKNAME + " " + NICKNAME)
    send_data('NICK ' + NICKNAME)
    joinchan(CHANNEL)
    send_data('PRIVMSG candy !ep2')
    while (1):
        ircmsg = IRC.recv(2048).decode("UTF-8")
        # DEBUG # print(ircmsg)
        data = ircmsg.split(':')[2]
        decoded = base64.b64decode(data).decode("UTF-8") 
        IRC.send(bytes("PRIVMSG candy !ep2 -rep %s" % decoded + '\n', 'UTF-8'))
        ircmsg = IRC.recv(2048).decode("UTF-8")
        print('Password: %s' % ircmsg.split('password ')[1])


main()
