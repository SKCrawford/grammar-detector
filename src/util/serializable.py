from json import dumps


class Serializable:
    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=2)
