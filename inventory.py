""" Program to managing inventory and making decisions from it

This program basically deals with the managing products along with ingredients required to make it.
Also, it does follwing-

"""
import csv
import collections as clt
import operator 
from operator import itemgetter

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
		# print (self.ingredients)
		# Read Sales
		with open('sales.csv', 'r') as sales_fp:
			temp_sales = list(csv.DictReader(sales_fp))
			# Convert day,quantity_sold,zipcode to Int
			self.sales = map(lambda x: {'product_id': x['product_id'],
				'day': int(x['day']),
				'quantity_sold': int(x['quantity_sold']),
				'zipcode': x['zipcode']},temp_sales)

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
		# print ("HARRY POTTER")
		# print self.inventory_history

	def get_top_products(self, limit=5, day=9):
		""" Method which gives list of n top selling products on a particular day.
		Arguments:
			limit - Limit for ranks of products 
			day - Particular day on which revenue is to be calculated

		Returns:
			result - List of dictonary of product and respective revenue within given limit
			Example - [{'product': {'price': 14, 'id': '827393e5'},'revenue': 1330},
				{'product': {'price': 14, 'id': '4b7c45dd'}]
		"""
		product_revenue = clt.defaultdict(int)
		for transaction in self.sales:
			if transaction['product_id'] in self.products.keys() and transaction['day'] == day:
				product_revenue[transaction['product_id']] = product_revenue[transaction['product_id']] +\
				(transaction['quantity_sold'] * self.products[transaction['product_id']])
			else:
				continue

		result = []
		for product in sorted(product_revenue.items(), key=operator.itemgetter(1), reverse = True):
			result.append({'product' : {'id' : product[0], 'price' : self.products[product[0]]}, 'revenue': product[1]})
		return result[:limit]

	def __get_product_revenues_till_now(self):
		product_revenue = clt.defaultdict(int)
		for transaction in self.sales:
			if transaction['product_id'] in self.products.keys():
				product_revenue[transaction['product_id']] += (transaction['quantity_sold'] * self.products[transaction['product_id']])
			else:
				continue
		return product_revenue

	def zipcode_revenue_mapping(self, range_of_days):
		""" Method mapping zipcode with range of days [start, end]
		Arguments:
			range_of_days - tuple of [start, end]

		Returns:
			List containing zipcode mapped with revenue within open range of days
		"""
		zipcode_revenue = clt.defaultdict(int)
		
		start_day = range_of_days[0]
		end_day =  range_of_days[1]

		for transaction in self.sales:
			if transaction['day'] in range(start_day, end_day + 1):
				zipcode_revenue[transaction['zipcode']] += (transaction['quantity_sold'] * self.products[transaction['product_id']])
		return [{'zipcode': x[0], 'revenue':x[1] } for x in zipcode_revenue.iteritems()]

	def get_depletion_rate(self, ingredient):
		""" Calculates the depletion rate of the ingredient w.r.t. ingredient history only

		Arguments:
			ingredient - ID of ingredient

		Returns:
			Rate of depletion of given ingredient
		"""
		rate_of_depletion = 0.0
		inventory_record = []
		# ingredient_id,day,units_in_inventory
		for example in self.inventory_history:
			if example['ingredient_id'] == ingredient:
				inventory_record.append({'day': example['day'], 'units_in_inventory': example['units_in_inventory']})

		inventory_sorted_by_timeline = [(i['day'], i['units_in_inventory'])
			for i in sorted(inventory_record, key=itemgetter('day'))]

		# print inventory_sorted_by_timeline
		start_day = 0
		count = 0 
		min_order_size = self.ingredients[ingredient]['min_order_size']
		# print ("min_order_size" +  str(min_order_size))
		for index, tup in enumerate(inventory_sorted_by_timeline):
			if tup[0] == 0:
				# print "first step babby"
				# print "vontinue"
				continue
			elif tup[1] == min_order_size:
				# get previous units in inventory and end day
				end_day = inventory_sorted_by_timeline[index - 1][0]
				# print "end day " +  str(end_day)
				if count > 0:
					count += 1
					current_rate = float(min_order_size - inventory_sorted_by_timeline[index - 1][1])/ float(end_day - start_day + 1)
					rate_of_depletion = ((rate_of_depletion * (count - 1)) + current_rate)/ count
					start_day = inventory_sorted_by_timeline[index][0]
					# print rate_of_depletion
				elif count == 0:
					# print "count 0 "
					# print "start day " + str(start_day)
					# print "last value " + str(inventory_sorted_by_timeline[index - 1][1])
					# print "min_order_size " + str(min_order_size)
					count = 1
					rate_of_depletion = float(min_order_size - inventory_sorted_by_timeline[index - 1][1])/ float(end_day - start_day + 1)
					# print ("harry")
					# print rate_of_depletion
					start_day = inventory_sorted_by_timeline[index][0]
					# print rate_of_depletion
			else:
				# print " continue"
				continue
		# print "rate_of_depletion" + str(rate_of_depletion)
		return rate_of_depletion

	def __profile_ingredients(self):
		""" 
		"""
		# Filter all ingredients which are already full. May be not. This is because of min_order_size is minimum, 
		# not upper bound

		# Now, discard ingredients which are not required in any product
		ingredients_in_use = set()
		for record in self.mapping:
			ingredients_in_use.add(record['ingredient_id'])

		profiler_ingredient = [] # profiler for ingredients
		product_ingredients = clt.defaultdict(dict) # dict for products and its ingredients

		for ingredient in ingredients_in_use:
			temp_product = set()
			for record in self.mapping:
				product_ingredients[record['product_id']][record['ingredient_id']] = record['quantity']
				if record['ingredient_id'] == ingredient:
					temp_product.add(record['product_id'])

			# GET USABILITY FACTOR i.e. in how many products the ingredient was used
			usability = len(temp_product)

			# GET REVENUE FACTOR
			# how much revenue the ingredient has contributed so far in all products?
			product_revenue_list = self.__get_product_revenues_till_now()

			# get total product content (sum of all contents), and contribution of 
			product_totl_content = {}
			contribution = 0.0
			for product in temp_product:
				product_totl_content[product] = sum(product_ingredients[product].values())
				contribution += product_revenue_list[product] * float(product_ingredients[product][ingredient])/ float(product_totl_content[product])
			revenue_factor = contribution

			# GET COST FACTOR
			cost_factor = self.ingredients[ingredient]['price_per_unit']

			profiler_ingredient.append({'ingredient': ingredient,
				'depletion_rate':self. get_depletion_rate(ingredient),
				'usability': usability,
				'revenue_factor': revenue_factor,
				'cost_factor': cost_factor})
		return profiler_ingredient
	
	def get_top_ingredients_to_order(self, limit):
		"""
		"""
		profiler = self.__profile_ingredients()

		# Normalize all paramters. Here, we are not considering any weight for any parameter. 
		# Every parameter is of same weight and normalized in [0,1]
		max_depletion_rate = float(max([x['depletion_rate'] for x in profiler]))
		max_usability = float(max([x['usability'] for x in profiler]))
		max_revenue_factor = float(max([x['revenue_factor'] for x in profiler]))
		max_cost_factor = float(max([x['cost_factor'] for x in profiler]))

		ranked_ingredients = {}
		for record in profiler:
			normalized_depletion_rate = float(record['depletion_rate'])/ max_depletion_rate
			normalized_usability = float(record['usability'])/ max_usability
			normalized_revenue_factor = float(record['revenue_factor'])/ max_revenue_factor
			normalized_cost_factor = float(record['cost_factor'])/ max_cost_factor
			ranked_ingredients[record['ingredient']] =  (normalized_depletion_rate *
				normalized_usability *
				normalized_revenue_factor)/normalized_cost_factor
		# for i,j in sorted(ranked_ingredients.items(), key=operator.itemgetter(1), reverse = True):
		# 	print i + " " + str(j)
		return sorted(ranked_ingredients.items(), key=operator.itemgetter(1), reverse = True)[:limit]
			
if __name__ == '__main__':
	i = Inventory()
	print i.get_top_products(limit=5, day=4)

	print 

	print i.zipcode_revenue_mapping((1,5))
	# print i.get_top_ingredients_to_order(10)
