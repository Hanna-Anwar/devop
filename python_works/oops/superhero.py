class SuperHeroes:

    name : str

    super_powers : str

    universe  : str


    def set_super_hero(self,name,super_powers,universe):

        self.name = name

        self.super_powers = super_powers

        self.universe = universe

    def display(self):

        print(self.name,self.super_powers,self.universe)

batman_instance = SuperHeroes()

batman_instance.set_super_hero("BATMAN","run,fly,rich","dc")

batman_instance.display()

minnalmurali_instance = SuperHeroes()

minnalmurali_instance.set_super_hero("MINNALMURALI","run,stremngth","Basilunu=iverse")

minnalmurali_instance.display()    