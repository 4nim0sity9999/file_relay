class DataviewError(Exception):
    pass

class PathNotExistErr(DataviewError):
    def __init__(self, path,key):
        self.path = path
        self.key = key
        super().__init__(f"路径'{self.path}'中的键'{self.key}'不存在")


class DictView:
    def __init__(self,data:dict,path:str):
        self._data = data
        self.path = path.split(".")
    
    def __repr__(self):
        return self.get()
    
    def __len__(self):
        return len(self.get())
    
    def get(self) -> str:
        value = self._data
        for i in self.path:
            # if i not in value:
            #     raise PathNotExistErr('.'.join(self.path),i)
            value = value[i]

        return value