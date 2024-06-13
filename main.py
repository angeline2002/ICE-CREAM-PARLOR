from functions import add_to_cart, search_offerings, add_allergen, view_cart

def main():
    user_id = 1  # Assuming a single user for simplicity
    
    while True:
        print("\nIce Cream Parlor Cafe")
        print("1. View Seasonal Offerings")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Add Allergen")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            season = input("Enter season (or leave blank for all): ")
            offerings = search_offerings(season)
            print("\nAvailable Flavors:")
            for flavor in offerings:
                id, name, season, allergens = flavor
                allergens_text = allergens if allergens else "None"
                print(f"{id} - {name} ({season}) - Allergens: {allergens_text}")
        
        elif choice == '2':
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            add_to_cart(user_id, flavor_id)
            print("Flavor added to cart!")
        
        elif choice == '3':
            cart = view_cart(user_id)
            print("\nYour Cart:")
            for item in cart:
                print(item[0])
        
        elif choice == '4':
            allergen = input("Enter allergen to add: ")
            add_allergen(allergen)
            print("Allergen added!")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
