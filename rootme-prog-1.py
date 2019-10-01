import socket, string, time, math
SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = 'Ck4aM-bot3'
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
        ircmsg = ircmsg.strip('nr')
        # DEBUG # print(ircmsg)


def racine(nb1, nb2):
    return round(float(math.sqrt(float(nb1)) * float(nb2)), 2)


def Listener():
    send_data("USER " + NICKNAME + " " + NICKNAME + " " + NICKNAME + " " + NICKNAME)
    send_data('NICK ' + NICKNAME)
    joinchan(CHANNEL)
    send_data('PRIVMSG candy !ep1')
    while (1):
        ircmsg = IRC.recv(2048).decode("UTF-8").strip('nr')
        # DEBUG # print(ircmsg)
        nbs = ircmsg.split(':')[2].split(' / ')
        IRC.send(bytes("PRIVMSG candy !ep1 -rep %s" % racine(nbs[0], nbs[1]) + '\n', 'UTF-8'))
        ircmsg = IRC.recv(2048).decode("UTF-8").strip('nr')
        print('Password: %s' % ircmsg.split('password ')[1])


main()
