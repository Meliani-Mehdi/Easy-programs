class Casey:
    def sentenceCase(self, text):
        latters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        t = True
        ren = ''
        for l in text:
            if l == ' ':
                t = True
                ren+=l
            elif t and l in latters:
                t = False
                ren+=l.upper()
            else:
                ren+=l.lower()
        return ren

    def altCase(self, text):
        pass

    def upperCase(self, text):
        return text.upper()

    def lowerCase(self, text):
        return text.lower()

    def titleCase(self, text):
        return text.title()

    def inverseCase(self, text):
        invText=""
        for l in text :
            if( l.isalpha()):
                if(l.isupper()):
                    l.lower()
                else:
                    l.upper()
    def reverseCase(self, text):
        revText=""
        for l in text :
            revText=+l
        return revText

    def capitalizedCase(self, text):
        return text.capitalize()



if __name__ == "__main__":

    pass
