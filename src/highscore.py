class HighScore:
    """Manages the top 10 best results."""

    def __init__(self, path):
        """Initialize everything."""
        print(__file__)
        self.path = path

    @property
    def highscore(self):
        """Get the highscore from file."""
        try:
            with open(self.path, 'r') as file:
                return [line.strip().split(';') for line in file]
        except IOError:
            return []

    def write_file(self, highscore):
        """Write the highscore to file."""
        with open(self.path, 'w') as file:
            for result, name, date in highscore:
                file.write('{result};{name};{date}\n'.format(result=result, name=name, date=date))

    def in_top_10(self, result):
        """Check if a results qualifies for the top 10 list."""
        highscore = self.highscore
        if len(highscore) < 10:
            return True
        if int(result) > int(highscore[-1][0]):
            return True
        return False

    def add_result(self, result, name, date):
        """Add a result to the top 10 list."""
        entry = [result, name, date]
        highscore = self.highscore
        highscore.append(entry)
        highscore.sort(reverse=True, key=lambda x: (int(x[0]), x[1], x[2]))
        self.write_file(highscore[:10])
        return highscore.index(entry)
