class FileReader(object):
    def __init__(self, PATH='file_reader_test.txt'):
        self.PATH = PATH
        self.digraph = None
        self.verticies = []
        self.edges = []
        if self.PATH is not None:
            self._graph_or_digraph()
            self._read_file()

    def _graph_or_digraph(self):
        f = open(self.PATH, "r")
        first_char = f.read(1)
        if first_char == 'G':
            self.digraph = False
        elif first_char == 'D':
            self.digraph = True
        else:
            raise Exception(f"File must begin with G or D, found {first_char}")
        f.close()

    def _read_file(self):
        f = open(self.PATH, "r")
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                continue
            elif i == 1:
                self.verticies = line.split(',')
            else:
                tuple_line = self.line_to_tuple(line)
                self.edges.append(tuple_line)
        f.close()
        return self.verticies, self.edges

    # def line_to_tuple(self, line):
    #     # O(n) solution
    #     stack = []
    #     start = True
    #     for char in line:
    #         if char == '(' or char == ')':
    #             continue
    #         elif char == ',':
    #             start = True
    #         else:
    #             if start:
    #                 stack.append(char)
    #                 start = False
    #             else:
    #                 stack.append(stack.pop() + char)
    #     return tuple(stack)

    def line_to_tuple(self, line):
        '''Python's built in methods are 150% faster!'''
        return tuple(line[1:-1].split(','))
