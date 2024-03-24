class Token:
    def __init__(self,  name, type, pos, id = None,):
        self.id = id
        self.name = name
        self.type = type
        self.pos = pos
