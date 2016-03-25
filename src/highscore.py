class HighScore:
    def __init__(self, path):
        print(__file__)
        self.path = path

    @property
    def highscore(self):
        try:
            with open(self.path, 'r') as file:
                return [line.strip().split(';') for line in file]
        except IOError:
            return []

    def write_file(self, highscore):
        with open(self.path, 'w') as file:
            for result, name, date in highscore:
                file.write('{result};{name};{date}'.format(result=result, name=name, date=date))

    def add_result(self, result, name, date):
        entry = (result, name, date)
        highscore = self.highscore
        highscore.append(entry)
        highscore.sort(reversed=True)
        self.write_file(highscore)
        return highscore.index(entry)
