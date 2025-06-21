class person:
    def __init__(self):
      print("hey i am aperson")

      def info(self):
          print(f"{self.name} is a {self.occ}")   # type: ignore

a=person()
a.name='divya'
a.occ="hr"
# a.info()
        