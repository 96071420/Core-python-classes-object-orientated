compression_plugins ={...}
extension_map = {...}

class multireader:
    def __init__(self, filename):
        extension = os.path.splittext(filename) [1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
     self.f.close()

     def read(self):
         return self.f.read()



