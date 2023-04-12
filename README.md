# Phase 3 Mock Code Challenge - Grocery

For this challenge, we'll be working with a domain similar to a grocery store.

We have one model: `FoodItem` which shows the items available at our store.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Your tables have not been created yet. In order to build them, first use
`python debug.py` and then use the class method `FoodItem.create_table()`.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

- `FoodItem __init__(name, price, id=None)`
  - `FoodItem` is initialized with a name (string) and a price (float)
  - A float in the database is called a REAL
  - Assume that FoodItems will always be initialized with the proper data types
- `FoodItem __repr__()`
  - Returns the FoodItem instance in the format below:
  - `<FoodItem id={id} name={name} price={price}>`
- `FoodItem property price()`
  - Returns the `FoodItem`'s price
  - Price must be a float larger than 0

### SQL Methods

- `FoodItem save()`
  - Creates a FoodItem in the database if a FoodItem with the same id doesn't exist
  - Updates a FoodItem in the database if a FoodItem with the same id exists
- `FoodItem increase_price(increase)`
  - Increments the price of the FoodItem by the `increase` parameter
  - This should be reflected in both the instance and the database
- `FoodItem classmethod query_all()`
  - Returns a list of FoodItem instances based on rows in the database
  - The return value ought to be a list of FoodItem instances

### BONUS Methods

- `FoodItem classmethod query_average_price()`
  - Returns a number that is the average of all food item prices in the database
  - Average is determined by the total sum of prices divided by the number of items
