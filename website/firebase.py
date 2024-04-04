import pyrebase
from . import firebase_config

firebase = pyrebase.initialize_app(firebase_config.config)
db = firebase.database()
storage = firebase.storage()
auth = firebase.auth()

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class User:
    def __init__(self):
        self.__user = None
        self.__password = None

    def update_value_db(self, value):
        db.child("Data").child(self.__user).update(value)

    def loggin(self):
        for i in get_all_values_db():
            if (
                i.val().get("username") == self.__user
                and i.val().get("password") == self.__password
            ):
                return True
        return False

    def register(self):
        pass

    def get_post(self):
        values = db.child("Data").child(self.__user).child("post").get()
        if values.val() == None:
            return None
        post = []
        for i in values:
            if i.val() == None:
                return None
            post.append(
                Namespace(title=i.val()["title"], description=i.val()["description"], img=i.val()["img"])
            )
        return post

    def add_post(self, title, description, img):
        storage.child(f"{self.__user}/{self.__user}_{title}.jpg").put(img)
        data = {"title": title, "description": description, "img": self.get_url(title)}
        db.child("Data").child(self.__user).child("post").push(data)

        return

    def get_url(self, title):
        return storage.child(f"{self.__user}/{self.__user}_{title}.jpg").get_url(None)

    def set_user(self, user: str, password: str):
        self.__user = user
        self.__password = password

def get_all_values_db():
    return db.child("Data").get().each()

Kurumi = User()
Kurumi.set_user("Kurumi", "123456")

def main():
    # data = {"username": username, "password": password, "post": {}}
    # db.child("Data").child(username).set(data)
    for i in Kurumi.get_post():
        print(i)


if __name__ == "__main__":
    main()
