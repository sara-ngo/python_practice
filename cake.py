class Cake:
    cake_type = ["choc_cake", "redv_cake", "lemo_cake"] # fill this in the order of 'type' e.g if type = 3 represents lemon cake then cake_type[type - 1] = "lemon_cake"
    recipe = {
        "choc_cake": {
            "Flour": 15.8,
            "Sugar": 24.5,
            "Unsweetened cocoa powder": 5.6,
            "Baking powder":0.4,
            "Baking soda": 0.6,
            "Salt": 0.4,
            "Egg": 9.0,
            "Buttermilk": 18.0,
            "Oil": 8.1,
            "Vanilla extract": 0.6,
            "Boiling extract": 17.0,},

        "redv_cake": { 
            "Flour": 22.4,
            "Sugar": 22.4,        
            "Unsweetened cocoa powder": 0.4,
            "Baking soda": 0.7,
            "Salt": 0.4,
            "Egg": 9.0,
            "Buttermilk": 17.9,
            "Oil": 24.0111,
            "Vanilla extract": 0.3,
            "Red food coloring": 2.1,
            "Distilled vinegar": 0.4,},

         "lemo_cake": {
            "Sugar": 15.0,
            "Egg": 9.0,
            "Buttermilk": 9.0,
            "Vanilla extract": 0.2,
            "Butter": 8.5,
            "Sifted self rising flour": 15.6,
            "Filling - Egg Yolk": 17.9,
            "Filling - Sugar": 11.3,
            "Filling - Butter": 2.1,
            "Filling - Lemon zest": 11.4,}
         }

# for printing the desired output we can use a separate list for fillings, just for convenience
    filling = {"choc_cake": [], # fill the items that are meant to be fillings here,
                "redv_cake": [], # fill the items that are meant to be fillings here,
                "lemo_cake": []
                }

    def __init__(self, type, size): # constructor
        self.type = type
        self.size = size
        self.name = ""
        self.weight = 0.0
        self.ingrd_list = []
    
    # getters for getting values from the object we called at the bottom of this file
    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getWeight(self):
        return self.weight

    # setter for assigning new values we just calculated to the object
    def setData(self, type, size, name, weight):
        self.type = type
        self.size = size
        self.name = name
        self.weight = weight

    def calc_ingrd(self, weight, recipe):
        self.ingrd_list.append(list(recipe.keys())) # takes ingrd name from recipe and inserts into ingrd_list[]
        wt_list = []
        for key in self.ingrd_list[0]:
            amount = float((weight * float(recipe[key]) * 16 / 100))
            wt_list.append(amount)
            self.ingrd_list.append(wt_list) # after calculate the amount, inserts into ingrd_list[]
        return wt_list 

    def __str__(self):
        recipe = ""
        size_word = ""
        if self.type == 1:
            recipe = "Chocolate Cake"
        elif self.type == 2:
            recipe = "Red Velvet Cake"      
        else:
            recipe = "Lemon Cake"

        if self.getSize() == 'L':
            size_word = "Large"             
            weight = 7
        else:
            size_word = "Small"
            weight = 4
        header = "Ingredient Quantities for %s %s \n\n" % (size_word, recipe)
        self.calc_ingrd(weight, Cake.recipe[Cake.cake_type[self.type - 1]]) # calc_ingrd(self, weight, recipe)
        for i in range(len(self.ingrd_list[0])):   
            # :<28 for left-justified 28 characters' spaces 
            # :.1 for 1 number after decimal sign
            header += "{:<28} {:.1f} Oz\n".format(self.ingrd_list[0][i], self.ingrd_list[1][i]) # 0: name; 1: amount
        return header

my_lrg_lemon_cake = Cake(3, 'L') # call a cake object
print(my_lrg_lemon_cake)

my_reg_lemon_cake = Cake(3, 'R')
print(my_reg_lemon_cake)

my_lrg_choc_cake = Cake(1, 'L')
print(my_lrg_choc_cake)

my_reg_choc_cake = Cake(1, 'R')
print(my_reg_choc_cake)

my_lrg_redv_cake = Cake(2, 'L')
print(my_lrg_redv_cake)

my_reg_redv_cake = Cake(2, 'R')
print(my_reg_redv_cake)