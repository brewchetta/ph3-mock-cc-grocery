from lib import CONN, CURSOR

class FoodItem:
    # THIS METHOD WILL CREATE THE SQL TABLE #
    @classmethod
    def create_table(cls):
        create_food_items_sql = """CREATE TABLE IF NOT EXISTS food_items (
        id INTEGER PRIMARY KEY, name TEXT, price REAL
        )
        """
        CURSOR.execute(create_food_items_sql)

    # ADD YOUR CODE BELOW #
    def __init__(self, name, price, id = None):
        self.name = name
        self.price = price
        self.id = id

    def __repr__(self):
        return f"<FoodItem id={self.id} name={self.name} price={self.price}>"
    
    def get_price(self):
        if hasattr(self, "_price"):
            return self._price
        else:
            print("Price is invalid")

    def set_price(self, price):
        if isinstance(price, float) and price > 0:
            self._price = price
        else:
            print("INFLATION IS REAL WAHHHHHH")
    
    price = property(get_price, set_price)

    def save(self):
        if self.id:
            self._update()
        else:
            self._create()
    
    def _create(self):
        sql = """INSERT INTO food_items (name, price) VALUES (?, ?)"""

        CURSOR.execute(sql, [self.name, self.price])
        CONN.commit()

        self.id  = CURSOR.execute("""SELECT id FROM food_items ORDER BY id DESC""").fetchone()[0]

    def _update(self):
        sql = """UPDATE food_items SET name = ?, price = ? WHERE id = ?"""

        CURSOR.execute(sql, [self.name, self.price, self.id])
        CONN.commit()

    def increase_price(self, increase):
        if isinstance(increase, (float, int))  and increase > 0:
            self.price += increase
            self.save()
        else:
            print("increase must be a number")
    
    @classmethod
    def query_all(cls):
        sql = """SELECT * FROM food_items"""
        all_items = CURSOR.execute(sql).fetchall()
        items_list = []
        for item in all_items:
            item = FoodItem(item[1], item[2], item[0])
            items_list.append(item)
        return items_list

    @classmethod
    def query_average_price(cls):
        all = FoodItem.query_all()
        prices = [food.price for food in all]
        return sum(prices)/len(prices)
    
    # alternate query_average_price function
    # @classmethod
    # def query_average_price(cls):
    #     sql = """SELECT AVG(price) FROM food_items"""
    #     result = CURSOR.execute(sql).fetchone()
    #     print(result)
    #     return result[0]