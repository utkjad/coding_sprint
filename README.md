Bevspot Coding Test
========
This project is intended to be open-ended and test your creativity and problem-solving skills. Feel free to use any programming language, however please make sure that your solution doesn't use external libraries, other than those included in the language's standard library. You may also use a library for CSV parsing. You should not use a database for this problem. We should be able to run the program you provide to us without additional installation steps.

Bevspot builds software for bars and restaurants to manage their inventory and track sales of their products. We've put together a zip file of fake sample data that includes:

* A list of ingredients and their minimum order quantities and price per unit (ingredients.csv)
* A list of products and their prices (products.csv)
* Ingredient inventory history (inventory_history.csv)
* Product sales by day and zipcode (sales.csv)
* A mapping of ingredient proportions to products in arbitrary units (mapping.csv)

Build a program that provides answers to the following questions. Prove that your answers are correct and/or describe how you would verify the validity of your program.

1. What are the top five selling products IDs on day four? How much revenue did they generate? (See below for an example of the output for day nine)
2. Write a function that returns a map of zipcodes to revenue for a given range of days.
3. Draw a diagram expressing the relationships of the data in the above model (you can draw it on paper or whiteboard, and include a photo.)
4. Write a function that estimates how fast an ingredient is being depleted based on inventory history
5. Write a function that determines which top ten ingredients the bar should order next. A few ideas for inputs to that decision:
  * Which ingredients are high-margin? One example of this would be an ingredient that is cheap per unit, but a lot of it is included in a high-revenue product.
  * Which ingredients will we run out of soon? Some ingredients are used up faster than others, and you can determine this with the inventory data history.
6. Bonus (if you have time): write a function that expresses a random product that could be made given a list of ingredient to product mappings, and a list of remaining ingredient inventory. How much would the product cost to make?

Submit your answers and code to us via email when you are done.

Example output
=====

Example Output for Problem 1:

Day nine's highest revenue products, and their revenue:

    [ { product: { id: '827393e5', price: 14 }, revenue: 1330 },
      { product: { id: '4b7c45dd', price: 14 }, revenue: 1162 },
      { product: { id: '03388d71', price: 14 }, revenue: 1078 },
      { product: { id: '93588de2', price: 13 }, revenue: 1014 },
      { product: { id: 'cb807f20', price: 13 }, revenue: 975 } ]
