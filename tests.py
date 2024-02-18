import unittest
import main


class TestFileOperation(unittest.TestCase):
    def setUp(self):
        data = ['Виктор Васкез: 15112005\n', 'Брюс Уэйн: 24092009\n']
        with open('test_file.txt', 'w') as file:
            for i in data:
                file.write(i)

    def test_get_data(self):
        instance = main.FileOperation('test_file.txt')
        instance.get_data()
        self.assertEqual(instance.raw_data[0], 'Виктор Васкез: 15112005\n')
        self.assertEqual(instance.raw_data[-1], 'Брюс Уэйн: 24092009\n')
        self.assertEqual(len(instance.raw_data), 2)

    def test_write_file(self):
        instance = main.FileOperation('test_file.txt')
        instance.write_file(['Виктор Васкез: 15112005\n'])

        with open('test_file.txt', 'r') as file:
            f = file.readline()

        self.assertEqual(f, 'Виктор Васкез: 15112005\n')


class TestSortingData(unittest.TestCase):
    def test_data_handler(self):
        instance = main.SortingData('test_file.txt')
        instance.data_handler()

        self.assertEqual(instance.data[0], ['Виктор', 'Васкез', '15112005'])

    def test_data_reset(self):
        instance = main.SortingData('test_file.txt')

        instance.final_data = [1, 2, 3]
        instance.raw_data = [1, 2, 3]
        instance.data = [1, 2, 3]
        instance.file = 'test.txt'

        instance.data_reset()

        self.assertEqual(instance.final_data, [])
        self.assertEqual(instance.raw_data, [])
        self.assertEqual(instance.data, [])
        self.assertEqual(instance.file, 'test_file.txt')

    def test_name_sort(self):
        instance = main.SortingData('test_file.txt')
        instance.name_sort()

        with open('name_sort_test_file.txt', 'r') as file:
            f = file.readlines()

        self.assertEqual(f[0], 'Брюс Уэйн: 24092009\n')
        self.assertEqual(f[-1], 'Виктор Васкез: 15112005\n')
        self.assertEqual(len(f), 2)

    def test_surname_sort(self):
        instance = main.SortingData('test_file.txt')
        instance.surname_sort()

        with open('surname_sort_test_file.txt', 'r') as file:
            f = file.readlines()

        self.assertEqual(f[0], 'Виктор Васкез: 15112005\n')
        self.assertEqual(f[-1], 'Брюс Уэйн: 24092009\n')
        self.assertEqual(len(f), 2)

    def test_telephone_sort(self):
        instance = main.SortingData('test_file.txt')
        instance.telephone_sort()

        with open('telephone_sort_test_file.txt', 'r') as file:
            f = file.readlines()

        self.assertEqual(f[0], 'Виктор Васкез: 15112005\n')
        self.assertEqual(f[-1], 'Брюс Уэйн: 24092009\n')
        self.assertEqual(len(f), 2)


if __name__ == '__main__':
    unittest.main()
