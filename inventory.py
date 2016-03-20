""" Program to managing inventory and making decisions from it

This program basically deals with the managing products along with ingredients required to make it.
Also, it does follwing-

"""
import csv
import collections as clt
import operator 

class Inventory(object):
	"""class managing Inventory for Products"""
	def __init__(self):
		""" Read path to the csv files and loads data into respective dictionaries"""

		# Read Products
		self.products = {}
		with open('products.csv', 'r') as products_fp:
			__ = products_fp.next()
			for product in products_fp:
				(product_id, product_price) = product.strip().split(',')
				self.products[product_id] = int(product_price)

		# Read ingredients
		self.ingredients = {}
		with open('ingredients.csv', 'r') as ingredients_fp:
			__ = ingredients_fp.next()
			for ingredient in ingredients_fp:
				(ingredient_id, ingredient_price_per_unit, ingredient_min_order_size) = ingredient.strip().split(',')
				self.ingredients[ingredient_id] = {
					'price_per_unit':int(ingredient_price_per_unit),
					'min_order_size': int(ingredient_min_order_size)}

		# Read Sales
		with open('sales.csv', 'r') as sales_fp:
			temp_sales = list(csv.DictReader(sales_fp))
			# Convert day,quantity_sold,zipcode to Int
			self.sales = map(lambda x: {'product_id': x['product_id'],
				'day': int(x['day']),
				'quantity_sold': int(x['quantity_sold']),
				'zipcode': int(x['zipcode'])},temp_sales)

		# Read mapping
		with open('mapping.csv', 'r') as mapping_fp:
			temp_mapping = csv.DictReader(mapping_fp)
			# Convert quantity to Int
			self.mapping = map(lambda x:  {'product_id': x['product_id'],
				'ingredient_id': x['ingredient_id'],
				'quantity': int(x['quantity'])},temp_mapping)

		# Read inventory_history
		with open('inventory_history.csv', 'r') as inventory_history_fp:
			temp_inventory_history = csv.DictReader(inventory_history_fp)
			# ingredient_id,day,units_in_inventory
			self.inventory_history = map(lambda x: {'ingredient_id': x['ingredient_id'],
				'day': int(x['day']),
				'units_in_inventory': int(x['units_in_inventory'])},temp_inventory_history)

	def get_top_products(self, rank=5, day=9):
		""" Method which gives list of n top selling products on a particular day.
		Arguments:
			rank - Rank limit, include product if its rank is >= given rank
			day - Particular day on which revenue is to be calculated

		Returns:
			result - List of dictonary of product and respective revenue
			Example - [{'product': {'price': 14, 'id': '827393e5'},'revenue': 1330},
				{'product': {'price': 14, 'id': '4b7c45dd'}]
		"""
		product_revenue = clt.defaultdict(int)
		for transaction in self.sales:
			if transaction['product_id'] in self.products.keys() and transaction['day'] == day:
				product_revenue[transaction['product_id']] = product_revenue[transaction['product_id']] + (transaction['quantity_sold'] * self.products[transaction['product_id']])
			else:
				continue
		result = []
		for product in sorted(product_revenue.items(), key=operator.itemgetter(1), reverse = True)[:rank]:
			result.append({'product' : {'id' : product[0], 'price' : self.products[product[0]]}, 'revenue': product[1]})
			# x = {'product' : {'id' : product[0], 'price' : self.products[product[0]]}, 'revenue': product[1]}
			# print x
		return result

	def zipcode_revenue_matching

if __name__ == '__main__':
	i = Inventory()
	print i.get_top_products()
