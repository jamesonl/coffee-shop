A online coffee retail simulator, used as practice for implementing microservice design patterns.

The goal of this exercise is to simulate how a real world online coffee retailer would implement a microservice architecture around a business.

To start, I'll need a name... henceforth, I am now the proud founder of **Five Harbors Coffee** _(the only coffee shop to procure coffee from all five continents)_!

## Requirements Development

I used a [`jamboard`](https://jamboard.google.com/d/1W54ugN3LCla95JbbANnSdRGNUEQuQWeBiFgux5uCTC4/viewer) to collect my thoughts about all the different things that I would pack into my software architecture diagram.

At the heart of my business, there are 4 kinds of objects:
 - Customers
 - The Warehouse
 - The Employees
 - The Bank

**Let's not forget...** this is a [`simulation`](https://en.m.wikipedia.org/wiki/Simulation). So there are also [game mechanics](https://en.m.wikipedia.org/wiki/Game_mechanics) that will need to be built as an additional layer to everything described here.

I won't get too much into the details of each of these units, but these are the things that services will be built around.

## Coffee Simulator

Before I can begin, I need ways of thinking about all of these four things.

### Customer Operation Principles

 - Customers can come and go
 - Each customer is unique, and has their own preferences
 - Our understanding of a customer's objective can - while imperfect - be quite close
 - _We can influence a customer's likelihood to churn through [`loyalty schemes`](https://en.wikipedia.org/wiki/Loyalty_program_)_

### Employee Operation Principles

 - Employees can come and go
 - Warehouse employees are contractors
 - Employees are part of core functions which impact the business in different ways
    - There are **3 core functions for this business**:
        - _Marketing_ - responsible for sourcing existing and new customer demand
        - _Warehouse Management_ - responsible for managing inventory, procuring new coffees, and managing contractors
        - _Shipping & Logistics_ - responsible for managing lead and delivery times for orders
 - **The core driver of success is getting these three groups to effectively work together!**

### The Warehouse Principles

 - Warehouses have limited inventory space
 - Warehouses and employees are responsible for the **storage of product**, **conversion of beans to bags**, and the **shipment of orders to customers**
 - Warehouses expand and contract in order to match existing demand
    - _If demand dries up (or the company stops investing in marketing), then the warehouse will need to respond in kind._

### Finance

 - Finance is responsible for keeping track of the company's accounts, order info, and customer info.
 - Finance is the _internal_ team, and cannot be borrowed from. They are strictly a reporting function. In the future, finance would be able to engage with the bank.

## Managing the Simulation

Since this is a simulation, game mechanics that we will need to consider include:

 - Time and Game Score
 - Player Actions and Events
 - Game Events and Interpretation
 - Saving Game Statistics

### Time and Game Score

 - All resources are bound by time; time is money
 - Players, Customers, and the Warehouse are all impacted by time, timeliness of operations, and the time between actions
 - As a function of the above two points... simulation score is impacted by:
    - **Maximize profit**, as a function of sales and cost
    - **Weather epochs** and **identify epochs**, as a function of new cycles, expansion, and contraction of business operation

### Player Actions

 - Action, and/or the lack thereof, statements of record that should be captured; The amount of action that a player generates does not impact game score alone
 - _Players can impact the underlying code that is provided to them in order to optimize the underlying processes._

### Game Events and Interpretation

 - `Epochs` impact players:
    - These are characterized by periods of high and low demand, and are somewhat random (for now).
    - The player needs to properly identify when these occur in order to maximize profitability.
 - `Business Analysis Report`: A player should be able to look back historically to determine the magnitude of the epoch.
 - `Market Research Report`: A player should can receive market information (at a cost) to determine how small or large the shock they experienced.

### Savings Game Statistics

 - Ultimately, this is an experiment to answer a few different questions:
    - **How does a player**:
        - value certain kinds of resources, functions, and/or actions?
        - prioritize changes to their business based on game events?
    - **How does the organization of the microservice architecture impact business operations?**
        - The way that I organized the underlying services is just a guess at **how a microservice architecture would be implemented** and **what would work best.**
    - **What kinds of `CODE` changes necessitate the greatest amount of change?**
        - This requires two sides... **the underlying ecosystem** within which a microservice lives, and the **microservice itself**.

## Game Organization

The starting structure of the game is composed of two services:

 - **The Online Ecosystem**
    - (Since this is _online_ ecosystem, we'll avoid typical problems about live communities...)
    - _Generate Customers_
    - _The Clock_
    - _Generate Epochs_
 - **Five Harbors**
    - Finance
    - Marketing
    - Warehouse
    - Shipping and Logistics
    - Employee Statistics
    - Customer Statistics


# Appendix

This is a list of the resources that I used in order to build this game.

## Resources and Descriptions

 - [List of Coffee Types](https://www.clarioncafe.com/coffee-bean-types/)
 - [World Map of Coffee Growing Regions](http://www.coffeeresearch.org/coffee/originsmap.htm) - I was not aware of where coffee really comes from... until I reviewed this map. The **coffee harvesting** time was also used in order to determine when certain kinds of coffee could be purchased.
 - [International Coffee Organization](http://www.ico.org/) - used this for research on current events.
