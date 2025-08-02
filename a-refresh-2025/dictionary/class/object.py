class Animal:
    name = "piglet"
    cry = "Oink"
    final = "..."
    def speak(self):
        print("{}! I'm {}! {}!".format(self.cry, self.name, self.final))

hamlet = Animal()  #instance
hamlet.name = "Hamlet"  #instance variable
hamlet.cry = "Oink oink"

hamlet.speak()  #method

lamb = Animal()
lamb.name = "Lamb"
lamb.cry = "Mmeeh mmeeeh"

lamb.speak()