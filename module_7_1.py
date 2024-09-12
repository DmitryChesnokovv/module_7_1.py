class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name, self.weight, self.category) == (other.name, other.weight, other.category)
        return False

    def __hash__(self):
        return hash((self.name, self.weight, self.category))


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
                file.close()
                return products
        except FileNotFoundError:
            return ''
    def add(self, *products):
        existing_products = self._get_existing_products()

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product not in existing_products:
                    file.write(str(product) + '\n')
                    existing_products.add(product)
                else:
                    print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
            file.close()

    def _get_existing_products(self):
        """Частный метод для получения набора объектов продуктов, которые уже есть в магазине."""
        products_in_shop = set()
        current_products = self.get_products()
        if current_products:
            for line in current_products.strip().split('\n'):
                name, weight, category = line.split(', ')
                products_in_shop.add(Product(name, float(weight), category))
        return products_in_shop


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  

s1.add(p1, p2, p3)

print(s1.get_products())
