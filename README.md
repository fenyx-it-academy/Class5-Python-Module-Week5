# Class5-Python-Module-Week5

# Week 5 Homework - OOP

## Question 1:
Create the class `Society` with following information:

`society_name`, `house_no`, `no_of_members`, `flat`, `income`

**Methods :**

*	 An `__init__` method to assign initial values of `society_name`, `house_no`, `no_of_members`, `income`
*	`allocate_flat()` to allocate flat according to income using the below table -> according to income, it will decide to flat type
*	`show_data()` to display the details of the entire class.
*   Create one object for each flat type, for each object call `allocate_flat()` and `show_data()`

| Income        | Flat           | 
| ------------- |:-------------:| 
| >=25000     | A Type | 
| >=20000 and <25000     | B Type      | 
| >=15000 and <20000 | C Type      |
| <15000 | D Type      |

## Question 2:
Define a class named `ItemInfo` with the following description:

`item_code`(Item Code), `item`(item name), `price`(Price of each item), `qty`(quantity in stock), `discount`(Discount percentage on the item), `net_price`(Price after discount)

**Methods :**
*	A member method `calculate_discount()` to calculate discount as per the following rules:
*	If `qty <= 10` —> discount is `0`
*	If `qty (11 to 20 inclusive)` —> discount is `15`
*	If `qty >= 20` —> discount is `20`
*	A constructor init method to assign the initial values for `item_code` to `0` and `price`, `qty`, `net_price` and `discount` to `null`
*	A function called `buy()` to allow user to enter values for `item_code`, `item`, `price`, `qty`. Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
*	A function `show_all()` or similar name to allow user to view the content of all the data members.


## Question 3:

Create a class called `Numbers`, which has a single class attribute called `multiplier`, and a constructor which takes the parameters `x` and `y` (these should all be numbers).

* Write a method called `add` which returns the sum of the attributes `x` and `y`.
* Write a class method called `multiply`, which takes a single number parameter `a` and returns the product of `a` and `multiplier`.
* Write a method called `subtract`, which takes two number parameters, `b` and `c`, and returns `b - c`.
* Write a method called `value` which returns a tuple containing the values of `x` and `y`. 
* Create a numbers object and call all the methods you wrote and print the results.
* 
## Question 4:

* Define the `Employee` class with an `__init__()` method
* Define a class variable `new_id` and set it equal to `1`
* Each Employee instance will need its own unique ID. Thus, inside `__init__()`, define `self.id` and set it equal to the class variable `new_id`
* Lastly, increment `new_id` by `1`
* Define a `say_id()` method
* Inside `say_id()`, output the string `"My id is "` and then the instance id.
* Define the variable e1 and set it to an instance of Employee
* Define the variable e2 and set it to an instance of Employee
* Have both e1 and e2 output their ids

## Question 5:

* Create a `Vehicle` class with `name`, `max_speed` and `mileage` instance attributes
* Add function `__str__` to vehicle class and print the info about vehicle as: `"Vehicle Model X has max speed 180 and mileage 12"`
* Create a child class `Bus` that will inherit all of the variables and methods of the `Vehicle` class
* Add attribute `capacity` to class `Bus`
* Update `Bus` class such that print message will be: `Bus Breng has max speed 180 and mileage 50 with capacity 100` (**Hint:** Override \__str__ method)
* Add `update_capacity()` method to the class `Bus`
* Create a `Vehicle` and a `Bus` object and print both of them
* call `update_capacity()` method for the earlier created `Bus` object and print it, see the difference

## HackerRank Questions

* **Inheritance:** https://www.hackerrank.com/challenges/inheritance/problem
  
* **Classes: Dealing with Complex Numbers:** https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
