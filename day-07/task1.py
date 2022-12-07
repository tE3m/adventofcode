import abc
from functools import cached_property


class FSObject(abc.ABC):
    name: str

    def __init__(self, object_name) -> None:
        self.name = object_name

    @abc.abstractmethod
    def size(self) -> int:
        pass


class Directory(FSObject):
    contents: list[FSObject]

    def __init__(self, directory_name):
        super().__init__(directory_name)
        self.contents = []

    def __repr__(self) -> str:
        return "Directory({}, {})".format(self.name, self.contents)

    @cached_property
    def size(self) -> int:
        return sum(element.size for element in self.contents)


class File(FSObject):
    _size: int

    def __init__(self, file_name, file_size) -> None:
        super().__init__(file_name)
        self._size = file_size

    def __repr__(self) -> str:
        return "File({}, {})".format(self.name, self.size)

    @cached_property
    def size(self) -> int:
        return self._size


if __name__ == '__main__':
    with open("input.txt") as file:
        output = [line.strip() for line in file.readlines()]
    directories: list[Directory] = []
    tree = Directory("/")
    path: list[Directory] = [tree]
    for line in output:
        if line[0] == "$":
            if line[2:4] == "cd":
                match line[5:]:
                    case "/":
                        path = [path[0]]
                    case "..":
                        path.pop()
                    case _:
                        directory = [directory for directory in path[-1].contents if directory.name == line[5:]][0]
                        assert type(directory) == Directory
                        path.append(directory)
        else:
            if line[:3] == "dir":
                directory = Directory(line[4:])
                path[-1].contents.append(directory)
                directories.append(directory)

            else:
                size, name = line.split(" ")
                file = File(name, int(size))
                path[-1].contents.append(file)
    print(sum(directory.size for directory in directories if directory.size <= 100000))
