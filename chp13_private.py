class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

        def public_method(self):
            #clients can use this
            pass

        def _unsafe_method(self):
            #clients shouldn't use this, but could if they wanted to
            pass
