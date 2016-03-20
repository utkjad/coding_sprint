""" Program to managing inventory and making decisions from it

This program basically deals with the managing products along with ingredients required to make it.
Also, it does follwing-

"""
import csv
import collections as clt

class Inventory(object):
	"""class managing Inventory for Products"""
	def __init__(self, path):
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
			self.sales = csv.DictReader(sales_fp)

		# Read mapping
		with open('mapping.csv', 'r') as mapping_fp:
			self.mapping = csv.DictReader(mapping_fp)

		# Read inventory_history
		with open('inventory_history.csv', 'r') as inventory_history_fp:
			self.inventory_history = csv.DictReader(inventory_history_fp)

	def 