class DAO:
    def __init__(self, datalist):
        self.datalist = datalist

    def create(self, data):
        self.datalist.append(data)
        return len(self.datalist)

    def read(self):
        return [itm for itm in self.datalist]

    def read_id(self, id_):
        return self.datalist[id_]
