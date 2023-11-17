// Let's start with a list of every ingredient we can think of



let egg = { name: "One Egg", category: "Dairy", quantity: 1, quantity_type: "egg", expires: 60};
let egg6 = { name: "Half-Dozen Eggs", category: "Dairy", quantity: 6, quantity_type: "egg", expires: 60}
let egg12 = { name: "A Dozen Eggs", category: "Dairy", quantity: 12, quantity_type: "egg", expires: 60}
let almondMilk = { name: "Almond Milk", category: "Dairy", quantity: 64, quantity_type: "fl. oz.", expires: 30 };
let butter = { name: "Butter", category: "Dairy", quantity: 1, quantity_type: "stick", expires: 180} // how am I going to log it when I need to convert one stick of butter into individual 
let butter_Tbsp = {name: "A Tablespoon of Butter", category: "Dairy", quantity: 1, quantity_type: "Tablespoon", expires: 180};
let chedder_cheese_sliced = { name: "Sliced Cheddar Cheese", category: "Dairy", quantity: 12, quantity_type: slices, expires: 30 };
let yogurt = { name: "Yogurt", category: "Dairy", quantity: 12, quantity_type: "oz." };


let apple = { name: "Apple", category: "Produce", quantity: 1, quantity_type: "apple" };
let banana = { name: "Banana", category: "Produce", quantity: 1, quantity_type: "banana" };
let oranges = { name: "Oranges", category: "Produce", quantity: 1, quantity_type: "orange" };
let grapes = { name: "Grapes", category: "Produce", quantity: 10, quantity_type: "oz." };
let strawberries = { name: "Strawberries", category: "Produce", quantity: 8, quantity_type: "oz." };
let blueberries = { name: "Blueberries", category: "Produce", quantity: 8, quantity_type: "oz." };
let watermelon = { name: "Watermelon", category: "Produce", quantity: 1, quantity_type: "watermelon" };
let mangoes = { name: "Mangoes", category: "Produce", quantity: 1, quantity_type: "mango" };
let pineapples = { name: "Pineapples", category: "Produce", quantity: 1, quantity_type: "pineapple" };
let kiwi = { name: "Kiwi", category: "Produce", quantity: 1, quantity_type: "kiwis" };
let peaches = { name: "Peaches", category: "Produce", quantity: 1, quantity_type: "peaches" };
let plum = { name: "Plum", category: "Produce", quantity: 1, quantity_type: "plum" };
let cherries = { name: "Cherries", category: "Produce", quantity: 16, quantity_type: "oz." };
let grapefruit = { name: "Grapefruit", category: "Produce", quantity: 1, quantity_type: "grapefruit" };
let avocado = { name: "Avocado", category: "Produce", quantity: 1, quantity_type: "avocado" };
let papaya = { name: "Papaya", category: "Produce", quantity: 1, quantity_type: "papaya" };
let pear = { name: "Pear", category: "Produce", quantity: 1, quantity_type: "pear" };
let cantaloupe = { name: "Cantaloupe", category: "Produce", quantity: 1, quantity_type: "cantaloupe" };
let honeydewMelon = { name: "Honeydew Melon", category: "Produce", quantity: 1, quantity_type: "honeydew melon" };
let raspberry = { name: "Raspberry", category: "Produce", quantity: 12, quantity_type: "oz." };
let blackberry = { name: "Blackberry", category: "Produce", quantity: 12, quantity_type: "oz." };
let lemon = { name: "Lemon", category: "Produce", quantity: 1, quantity_type: "lemon" };
let cranberries = { name: "Cranberries", category: "Produce", quantity: 12, quantity_type: "oz." };
let passionFruit = { name: "Passion Fruit", category: "Produce", quantity: 1, quantity_type: "passionfruit" };
let guava = { name: "Guava", category: "Produce", quantity: 1, quantity_type: "guava" };
let apricots = { name: "Apricots", category: "Produce", quantity: 1, quantity_type: "apricot" };
let nectarines = { name: "Nectarines", category: "Produce", quantity: 1, quantity_type: "nectarine" };
let carrot = { name: "Carrot", category: "Produce", quantity: 1, quantity_type: "carrot" };
let broccoli = { name: "Broccoli", category: "Produce", quantity: 1, quantity_type: "head" };
let tomato = { name: "Tomato", category: "Produce", quantity: 1, quantity_type: "tomato" };
let potato = { name: "Potato", category: "Produce", quantity: 16, quantity_type: "oz." };
let onion = { name: "Onion", category: "Produce", quantity: 1, quantity_type: "onion" };
let bellPepper = { name: "Bell Pepper", category: "Produce", quantity: 1, quantity_type: "pepper" };
let spinach = { name: "Spinach", category: "Produce", quantity: 16, quantity_type: "oz." };
let lettuce = { name: "Lettuce", category: "Produce", quantity: 16, quantity_type: "oz." };
let cucumber = { name: "Cucumber", category: "Produce", quantity: 1, quantity_type: "cucumber" };
let zucchini = { name: "Zucchini", category: "Produce", quantity: 1, quantity_type: "zucchini" };
let cauliflower = { name: "Cauliflower", category: "Produce", quantity: 1, quantity_type: "head" };
let brusselsSprouts = { name: "Brussels Sprouts", category: "Produce", quantity: 16, quantity_type: "oz." };
let greenBeans = { name: "Green Beans", category: "Produce", quantity: 16, quantity_type: "oz." };
let asparagus = { name: "Asparagus", category: "Produce", quantity: 12, quantity_type: "oz." };
let kale = { name: "Kale", category: "Produce", quantity: 16, quantity_type: "oz." };
let peas = { name: "Peas", category: "Produce", quantity: 16, quantity_type: "oz." };
let sweetPotato = { name: "Sweet Potato", category: "Produce", quantity: 1, quantity_type: "sweet potato" };
let corn = { name: "Corn", category: "Produce", quantity: 1, quantity_type: "ear" };
let celery = { name: "Celery", category: "Produce", quantity: 1, quantity_type: "stalk" };
let mushroom = { name: "Mushroom", category: "Produce", quantity: 12, quantity_type: "oz." };
let radish = { name: "Radish", category: "Produce", quantity: 1, quantity_type: "radish" };
let eggplant = { name: "Eggplant", category: "Produce", quantity: 1, quantity_type: "eggplant" };
let cabbage = { name: "Cabbage", category: "Produce", quantity: 1, quantity_type: "head" };
let garlic = { name: "Garlic", category: "Produce", quantity: 1, quantity_type: "bulb" };
let squash = { name: "Squash", category: "Produce", quantity: 1, quantity_type: "squash" };
let okra = { name: "Okra", category: "Produce", quantity: 1, quantity_type: "okra" };
let cilantro = { name: "Cilantro", category: "Produce", quantity: 1, quantity_type: "oz." };
let parsley = { name: "Parsley", category: "Produce", quantity: 1, quantity_type: "oz." };
let jalapeno = { name: "Jalapeno", category: "Produce", quantity: 1, quantity_type: "jalapeno" };
let greenOnionLeek = { name: "Green Onion/Leek", category: "Produce", quantity: 1, quantity_type: "bunch" };
let turnip = { name: "Turnip", category: "Produce", quantity: 1, quantity_type: "turnip" };
let rutabaga = { name: "Rutabaga", category: "Produce", quantity: 1, quantity_type: "rutabaga" };
let swissChard = { name: "Swiss Chard", category: "Produce", quantity: 1, quantity_type: "head" };
let bokChoy = { name: "Bok Choy", category: "Produce", quantity: 1, quantity_type: "head" };
let chickenBreast = { name: "Chicken Breast", category: "Meat" , quantity: 2, quantity_type: "breast"};
let chickenThigh = { name: "Chicken Thigh", category: "Meat",  };
let wholeChicken = { name: "Whole Chicken", category: "Meat" };
let groundBeef = { name: "Ground Beef", category: "Meat" };
let groundBison = { name: "Ground Bison", category: "Meat" };
let pasta = { name: "Pasta", category: "Pasta" };
let rice = { name: "Rice", category: "Grains" };
let pastaSauce = { name: "Pasta Sauce", category: "Condiments" };
let frozenPeas = { name: "Frozen Peas", category: "Frozen" };
let frozenVegetableMix = { name: "Frozen Vegetable Mix", category: "Frozen" };
let frozenCorn = { name: "Frozen Corn", category: "Frozen" };
let iceCream = { name: "Ice Cream", category: "Frozen" };
let breakfastCereal = { name: "Breakfast Cereal", category: "Cereal" };
let oatmeal = { name: "Oatmeal", category: "Cereal" };
let creamOfRice = { name: "Cream of Rice", category: "Cereal" };
let pancakeMix = { name: "Pancake Mix", category: "Bakery" };
let mapleSyrup = { name: "Maple Syrup", category: "Condiments" };
let coffee = { name: "Coffee", category: "Beverages" };
let tea = { name: "Tea", category: "Beverages" };
let sugar = { name: "Sugar", category: "Baking" };
let flour = { name: "Flour", category: "Baking" };
let cookingOil = { name: "Cooking Oil", category: "Condiments" };
let cannedSoup = { name: "Canned Soup", category: "Canned Goods" };
let cannedBeans = { name: "Canned Beans", category: "Canned Goods" };
let peanutButter = { name: "Peanut Butter", category: "Condiments" };
let jelly = { name: "Jelly", category: "Condiments" };
let jam = { name: "Jam", category: "Condiments" };
let ketchup = { name: "Ketchup", category: "Condiments" };
let mustard = { name: "Mustard", category: "Condiments" };
let bbqSauce = { name: "BBQ Sauce", category: "Condiments" };
let mayonnaise = { name: "Mayonnaise", category: "Condiments" };
let saladDressing = { name: "Salad Dressing", category: "Condiments" };
let snackCrackers = { name: "Snack Crackers", category: "Snacks" };
let chips = { name: "Chips", category: "Snacks" };
let salsa = { name: "Salsa", category: "Condiments" };
let tortillas = { name: "Tortillas", category: "Bakery" };
let deliTurkey = { name: "Deli Turkey", category: "Deli" };
let deliHam = { name: "Deli Ham", category: "Deli" };
let deliRoastBeef = { name: "Deli Roast Beef", category: "Deli" };
let frenchBread = { name: "French Bread", category: "Bakery" };
let bacon = { name: "Bacon", category: "Meat" };
let sausage = { name: "Sausage", category: "Meat" };
let sausageLink = { name: "Sausage Link", category: "Meat" };
let cumin = { name: "Cumin", category: "Spices" };
let cardamom = { name: "Cardamom", category: "Spices" };
let coriander = { name: "Coriander", category: "Spices" };
let italianSeasoning = { name: "Italian Seasoning", category: "Spices" };
let greenGoddess = { name: "Green Goddess", category: "Condiments" };
let onionPowder = { name: "Onion Powder", category: "Spices" };
let garlicPowder = { name: "Garlic Powder", category: "Spices" };
let bakingPowder = { name: "Baking Powder", category: "Baking" };
let chiliPowder = { name: "Chili Powder", category: "Spices" };
