from demo_app import app


class User(object):
    name = "Stranger"
    password = ""

    def checklogin(self, username, password):
        if username == app.config.get("ADMIN"):
            if password == app.config.get("PASSWORD"):
                return True
        return False

    def setname(self, username):
        self.name = username

    def setpw(self, password):
        self.password = password

    def destroy(self):
        self.setname("Stranger")
        self.setpw("-")