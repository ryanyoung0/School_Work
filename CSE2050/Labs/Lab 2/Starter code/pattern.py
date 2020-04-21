class Pattern:
    def __init__(self, pattern):
        self.pattern=pattern
    def set_case_sensitive(self, case):
        pass

    def findMatch(self, text, start = 0):
        self.text=text
        self.start=start
        return text.find(self.pattern, start)

    def findMatches(self, text):
        self.text = text
        text.upper()
        Matches=[]
        start=0
        for x in text:
            recurse = self.findMatch(text, start = start)
            if recurse == -1:
                break
            Matches.append(recurse)
            start = recurse + 1
        return Matches

    def __str__(self):
    	pass
