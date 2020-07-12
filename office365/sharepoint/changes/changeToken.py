from office365.runtime.clientValue import ClientValue


class ChangeToken(ClientValue):
    """Represents the unique sequential location of a change within the change log. Client applications can use the
    change token as a starting point for retrieving changes."""

    def __init__(self):
        super().__init__()
        self.StringValue = None
