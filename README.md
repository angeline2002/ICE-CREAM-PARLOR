# ICE-CREAM-PARLOR
 This Python application is designed to manage an ice cream parlor cafe, allowing users to view seasonal offerings, add flavors to their cart, view their cart, and add allergens. The application uses SQLite for data storage, making it easy to set up and use. It provides a simple and intuitive interface for customers to interact with the ice cream parlor's menu and manage their selections.


## Setup Instructions

### Running Locally

1. Set up the database:

    ```bash
    python database_setup.py
    ```

2. Insert initial data:

    ```bash
    python insert_initial_data.py
    ```

3. Run the main application:

    ```bash
    python main.py
    ```

### Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t icecream_parlor .
    ```

2. Run the Docker container:

    ```bash
    docker run -it --rm --name icecream_parlor_container icecream_parlor
    ```

The application will start, and you can interact with it via the terminal.

## Testing Steps

1. **View Seasonal Offerings**:
   - Choose option 1.
   - Enter a season or leave blank for all.
   - Verify the available flavors and their seasons.

2. **Add to Cart**:
   - Choose option 2.
   - Enter a flavor ID.
   - Verify that the flavor is added to the cart.

3. **View Cart**:
   - Choose option 3.
   - Verify the contents of your cart.

4. **Add Allergen**:
   - Choose option 4.
   - Enter a new allergen.
   - Verify that the allergen is added.

## SQL Queries or ORM Abstraction

All SQL queries are directly embedded in the functions defined in `functions.py`.

## Documentation of the Code

The code is documented with inline comments explaining the functionality of each section. Refer to `functions.py` and `main.py` for detailed documentation.
