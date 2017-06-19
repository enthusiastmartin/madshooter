class Level01(object):
    def __init__(self):
        self._entities = []

    def setup(self):
        pass

    @property
    def entities(self):
        return self._entities
