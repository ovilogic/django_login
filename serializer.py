from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):

        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='ovidiu.opreah@outlook.com', content='foo bar')