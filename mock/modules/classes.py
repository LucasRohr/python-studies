import os


class Helper:

    def __init__(self, path):
        self.path = path

    def get_path(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)


class Worker:

    PERCENTAGE = 0.5

    def __init__(self):
        self.helper = Helper('db')

    def calculate(self, price):
        return price * self.PERCENTAGE

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path

    def work_on_env(self):
        path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
        print(f'Working on {path}')
        return path

    def size_of(self):
        with open('text.txt') as f:
            contents = f.read()

        return len(contents)
