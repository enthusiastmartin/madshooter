class BaseLevel(object):
    def setup(self):
        pass

    def update(self, screen=None):
        pass

    @property
    def entities(self):
        return []
