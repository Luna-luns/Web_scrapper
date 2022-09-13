class LinkError(Exception):
    def __str__(self):
        return 'Invalid movie page!'
