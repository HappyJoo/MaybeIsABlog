# It was code for python3.5 
# And I'm using python3.7. So i guess that is the reason why it's not working
# But I'm still learning python, so i'll just leave it til i am better.
# 2019.4.3

import asynchat
import asyncore

# Setting port
PORT = 6666

# Creating endsession
class EndSession(Exception):
    pass

class ChatServer(asyncore.dispatcher):
    # ChatServer ~
    
    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        # create socket
        self.create_socket()
        # set socket to reuse
        self.set_reuse_addr()
        # listen port
        self.bind(('', port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


class ChatSession(asynchat.async_chat):
    # chat with clientserver

    def __init__(self, server, sock):
        asynchat.async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b'\n')
        self.date = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self, room):
        # delete from this room and add to another room
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_date(self, data):
        # collect date from client server
        self.data.append(data.decode("utf-8"))

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self, line.encode("utf-8"))
        except EndSession:
            self.handle_close()

    def handle_close(self):
        # when session close, enter LogoutRoom
        asynchat.async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))
            

class CommandHandler:
    # handler of command

    def unknown(self, session, cmd):
        # responds to unknown command
        # send message through asynchat.async_chat.push
        session.push(('Unknown command {} \n'.format(cmd)).encode("utf-8"))

    def handle(self, session, line):
        line = line.decode()
        # dealing command
        if not line.strip():
            return
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        method = getattr(self, 'do_' + cmd, None)
        try:
            method(session, line)
        except TypeError:
            self.unknown(session, cmd)

class Room(CommandHandler):
    # include many room

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        # append user
        self.sessions.append(session)

    def remove(self, session):
        # remove user
        self.sessions.remove(session)

    def broadcast(self, line):
        # broadcast message
        # use asynchat.async_chat.push to send
        for session in self.sessions:
            session.push(line)

    def do_logout(self, session, line):
        # logout
        raise EndSession


class LoginRoom(Room):
    # deal with login users

    def add(self, session):
        # respond to user successfully login
        Room.add(self, session)
        # push message
        session.push(b'Connect Success')

    def do_login(self, session, line):
        name = line.strip()
        # get user name
        if not name:
            session.push(b'UserName Empty')
        # check if there's an existed name
        elif name in self.server.users:
            session.push(b'UserName Exist')
        else:
            session.name = name
            session.enter(self.server.main_room)


class LogoutRoom(Room):
    # finish logout user
    
    def add(self, session):
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


class ChatRoom(Room):
    # room for chat
    def add(self, session):
        # broadcast new user
        session.push(b'login Success')
        self.broadcast((session.name + ' has entered the romm.\n').encode("utf-8"))
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        # broadcast the leaving of user
        Room.remove(self, session)
        self.broadcast((session.name + ' has left the room.\n').encode("utf-8"))

    def do_say(self, session, line):
        # send message to client server
        self.broadcast((session.name + 'has left the room.\n').encode("uft-8"))

    def do_look(self, session, line):
        # look online user
        session.push(b'Online Users:\n')
        for other in self.sessions:
            session.push((other.name + '\n').encode("utf-8"))

if __name__ == '__main__':
    
    s = ChatServer(PORT)
    try:
        print("chat server run at '0.0.0.0:{0}'".format(PORT))
        asyncore.loop()
    except KeyboardInterrupt:
        print("chat server exit")
