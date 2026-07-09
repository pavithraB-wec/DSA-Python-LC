class Codec:

    def __init__(self):
        self.url2id = {}
        self.id2url = {}
        self.id = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.url2id:
            self.id += 1
            self.url2id[longUrl] = str(self.id)
            self.id2url[str(self.id)] = longUrl
        return "http://tinyurl.com/" + self.url2id[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.split("/")[-1]
        return self.id2url[key]