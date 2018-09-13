class ProgrammingLanguage:
    def __init__(self, Field, Typing, Reflection, Year):
        self.Field = Field
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def __str__(self):
        # return (self.Field, self.Typing, self.Reflection, self.Year)
        return "{}{}{}{}".format(self.Field, self.Typing, self.Reflection, self.Year)

        # def __init__(self):
