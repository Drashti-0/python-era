class user:
    def __init__(self,name):
        self.name=name
        
class message:
    def __init__(self,user,text):
        self.user=user
        self.text=text
        
class chatroom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chatroom")

    def leave(self, user):
        self.users.remove(user)
        print(user.name, "left the chatroom")

    def send_message(self, user, text):
        message = Message(user, text)
        self.messages.append(message)
        print(user.name, ":", text)

    def chat_history(self):
        print("Chat History:")
        for message in self.messages:
            print(message.user.name, ":", message.text)