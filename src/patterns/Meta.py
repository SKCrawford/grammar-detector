class Meta:
    def __init__(self, *args, valid_keys=[], **kwargs):
        self._settings = {}
        self._valid_keys = valid_keys
        for k in kwargs:
            if len(valid_keys):
                if k in valid_keys:
                    self._settings[k] = kwargs[k]
            else:
                self._settings[k] = kwargs[k]

    def get_key(self, key):
        return self._settings[key]
