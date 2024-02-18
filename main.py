class FileOperation:
    def __init__(self, file):
        self.file = file
        self.raw_data = []

    def get_data(self):
        with open(self.file, 'r') as data:
            for item in data.readlines():
                self.raw_data.append(item)

    def write_file(self, result):
        with open(self.file, 'w') as data:
            for r in result:
                data.write(r)


class SortingData(FileOperation):
    def __init__(self, file):
        super().__init__(file)
        self.filename = self.file
        self.data = []
        self.final_data = []

    def data_handler(self):
        self.get_data()
        for item in self.raw_data:
            item = item.rstrip('\n')
            item = item.replace(':', '')
            self.data.append(item.split(' '))

    def data_reset(self):
        self.file = self.filename
        self.final_data = []
        self.raw_data = []
        self.data = []

    def name_sort(self):
        self.data_handler()

        result = sorted(self.data, key=lambda i: i[0])
        self.file = f'name_sort_{self.file}'

        for item in result:
            self.final_data.append(f'{item[0]} {item[1]}: {item[2]}\n')

        self.write_file(self.final_data)
        self.data_reset()

    def surname_sort(self):
        self.data_handler()

        result = sorted(self.data, key=lambda i: i[1])
        self.file = f'surname_sort_{self.file}'

        for item in result:
            self.final_data.append(f'{item[0]} {item[1]}: {item[2]}\n')

        self.write_file(self.final_data)
        self.data_reset()

    def telephone_sort(self):
        self.data_handler()

        result = sorted(self.data, key=lambda i: i[2])
        self.file = f'telephone_sort_{self.file}'

        for item in result:
            self.final_data.append(f'{item[0]} {item[1]}: {item[2]}\n')

        self.write_file(self.final_data)
        self.data_reset()
