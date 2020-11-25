def make_cake():
    REG_CAKE_WT = 4
    LAGRE_CAKE_WT = 7
    # Chocolate cake recipe; in percentage of total weight
    choc_recipe = { 
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
        "Boiling extract": 17.0,
    }

    # Red Velvet cake recipe; in percentage of total weight
    redv_recipe = {
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
        "Distilled vinegar": 0.4,
    }

    # Lemon cake recipe; in percentage of total weight
    lemon_recipe = {
        "Sugar": 15.0,
        "Egg": 9.0,
        "Buttermilk": 9.0,
        "Vanilla extract": 0.2,
        "Butter": 8.5,
        "Sifted self rising flour": 15.6,
        "Filling - Egg Yolk": 17.9,
        "Filling - Sugar": 11.3,
        "Filling - Butter": 2.1,
        "Filling - Lemon zest": 11.4,
        }

    def calc_ingrd(cake_wt, recipe):
        if cake_wt == 4:
            size_word = "Regular"
        else:
            size_word = "Large"
        if recipe == choc_recipe:
            print(( "%s Chocolate Cake Ingredients\n" % (size_word) ))
        elif recipe == redv_recipe:
            print(( "%s Red Velvet Cake Ingredients\n" % (size_word) ))
        else:
            print(( "%s Lemon Cake Ingredients\n" % (size_word) ))
        ingrd_list = list(recipe.keys())
        wt_list = []
        for x in ingrd_list:
            amount = float((float(recipe[x]) * cake_wt * 16.0) / 100)
            wt_list.append(amount)
        return wt_list
      
    def print_ingrd(ingrd_list, ingrd_names):
        for i in range(len(ingrd_list)):
            if(ingrd_list[i] != 0):
                print("%-28s%5.1f Oz" %(ingrd_names[i], round(ingrd_list[i],1)))

    """
    *******************************************************************************
                                        INPUT
    *******************************************************************************
    """

    cake_type = input("Please Select Cake Type; Enter 1 for Chocolate,"
                       " 2 for Red Velvet, 3 for Lemon, q to quit: ")

    if not( cake_type == 'q' or cake_type == 'Q' ):
        cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")

    while not(cake_type == 'q' or cake_type == 'Q'):
        print()
        cake_type = eval(cake_type)
                      
        if cake_type == 1:
            if cake_size == 'R' or cake_size == 'r':
                choc_cake_wt = REG_CAKE_WT
            elif cake_size == 'L' or cake_size == 'l':
                choc_cake_wt = LAGRE_CAKE_WT
            choc_ingrd_list = calc_ingrd(choc_cake_wt,choc_recipe)
            ingrd_names = list(choc_recipe.keys())
            print_ingrd(choc_ingrd_list,ingrd_names)
            print()
                    
        elif cake_type == 2:
            if cake_size == 'R' or cake_size == 'r':
                redv_cake_wt = REG_CAKE_WT
            elif cake_size == 'L' or cake_size == 'l':
                redv_cake_wt = LAGRE_CAKE_WT
            redv_ingrd_list = calc_ingrd(redv_cake_wt,redv_recipe)
            ingrd_names = list(redv_recipe.keys())
            print_ingrd(redv_ingrd_list,ingrd_names)
            print()

        else:
            if cake_size == 'R' or cake_size == 'r':
                lemo_cake_wt = REG_CAKE_WT
            elif cake_size == 'L' or cake_size == 'l':
                lemo_cake_wt = LAGRE_CAKE_WT
            lemon_ingrd_list = calc_ingrd(lemo_cake_wt,lemon_recipe)
            ingrd_names = list(lemon_recipe.keys())
            print_ingrd(lemon_ingrd_list,ingrd_names)
            print()
  
        cake_type = input("Please Select Cake Type; Enter 1 for Chocolate,"
                      " 2 for Red Velvet, 3 for Lemon, q to quit: ")
        if not (cake_type == 'q' or cake_type == 'Q'):
            cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")

    print()

make_cake()
