import streamlit as st

def scale_recipe(recipe, servings):
    scaled_recipe = {}
    for ingredient, amount in recipe.items():
        scaled_amount = amount * servings
        scaled_recipe[ingredient] = scaled_amount
    return scaled_recipe

def print_recipe(recipe):
    st.write("Brownie Recipe:")
    for ingredient, amount in recipe.items():
        st.write(f"- {amount:.2f} {ingredient}")

def main():
    # Original brownie recipe
    original_recipe = {
        " cup - Maida (all-purpose flour)": 0.125,
        " tbsp - Powdered sugar": 1.25,
        " tbsp - Cocoa powder": 1,
        " tbsp - Yogurt (curd)": 0.0625,
        " tbsp - Baking soda": 0.0625,
        " cup - Melted butter": 0.0625,
        " tbsp - Vanilla essence": 0.125,
        " cup - Walnuts": 0.0625  # Optional
    }

    # Sidebar for user input
    st.sidebar.header("Brownie Recipe Scaler")
    servings = st.sidebar.number_input("Enter the number of servings:", min_value=1, value=1)

    # Scale the recipe
    scaled_recipe = scale_recipe(original_recipe, servings)

    # Display the scaled recipe
    print_recipe(scaled_recipe)

if __name__ == "__main__":
    main()
