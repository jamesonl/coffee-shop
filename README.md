# coffee-shop

The core of this project is focused on **building a simulator**.

Concepts that I hope to touch on through this game include: #state, #[idempotency](https://www.restapitutorial.com/lessons/idempotency.html), #[simulation](https://simpy.readthedocs.io/en/latest/examples/index.html), #[microservices](https://www.fullstackpython.com/microservices.html), and #[system-design](https://thesystemsthinker.com/integrating-systems-thinking-and-design-thinking/).

## Main Objectives

 - create autonomous entities that a player can interact with... including:
    - `settlements`: composed of a population of varying demographics and preferences
    - `marketplaces`: which sell raw materials and are traded with in order to fulfill the worldwide _need(?)_ for coffee beans, and...
    - `consultants`: who sell information about the market to players.
 - see how a `player` decides to design their business in order to deal with the demand for coffee, and what they choose to do in order to _"win"_ the game.

## "Winning" the Game

 - Time is at the heart of our simulation - and thus, understanding how it is defined within our simulation is critical:
    - Time is organized into `epochs`, which are characterized specifically as, _"the beginning of a distinctive period in the history of someone or something."_
    - Epochs are configurable in length, and - depending on the preferences of the player(s) - can take the following shapes:
        - equally spaced ("X" duration) epochs, of a _determined_ duration; ends after "Y" number of epochs.
        - equally spaced ("X" duration) epochs, of an _indeterminate_ number of epochs.
        - _unequally_ spaced epochs, of a _specified_ number of epochs.
        - _unequally_ spaced epochs, of a _unspecified_ number of epochs.
 - Each `epoch` awards achievements to players inside the simulation based on their economic performance; both absolute and relative in nature... examples would include achievements like:
    - Most/Least Profitable
    - Most/Least Purchases
    - Most/Least Customers
    - Most/Least Ads
    - Best/Worst run Warehouse
    - Most/Least Informed Agency

>Success is determined by the player / player group, and not a strict adherence to any of the above single outcomes.

## Units of the Game

There are 4 main units within the game:

 - `Settlements` (see "Main Objectives")
 - `Marketplaces` (see "Main Objectives")
 - `Intelligence Agencies` (see "Main Objectives")
 - **`Players`** - **A player is some kind of a spectrum between a computer and a human.** Some players are computers, others are humans - some systems are the result of humans + computers... _it is up to the user to determine who and how others play!_

Implementations of each of these unit types can be found within the `ecosystem` folder.

## Developer Goals

 - The ability to capture [state](https://dev.to/karn/building-a-simple-state-machine-in-python) at any given point throughout the course of the simulation.
 - Developing a workflow for both GUI and programming based playing.
 - Capture state in such a way that I can answer core questions about the choices that players make decisions throughout the course of the game:
    - What assets and decisions are most critical to designing the most/least [insert achievement]?
    - How do different configurations of ecosystems influence the above?
    - How do human players vs. computer players differ in actions?

## Technology Stack

**The entire project will be developed in `Python`, and will leverage the following packages:**
 - `Flask` - this is a RESTFUL API framework that I can use to develop my application
 - `Celery` - this is a task management queue that I can use to store the state of my application throughout each simulation
 - `PyTest` - unit testing library for making sure that my methods work properly

**Non-Python Infrastructure that I'll also need to use:**
 - `Docker` - this will serve to host all the necessary tools / house the app
 - `RabbitMQ` - this will be the message broker responsible for managing the state of my application, delivering messages to different services

_note about the non-python infrastructure: I am developing everything locally right now. Developing for a server is **very** low priority_.

## References

Articles that I read throughout this process that I used as inspiration, or as a template for my own development:

 - [How to Build a Market Simulator Using Markov Chains and Python](https://towardsdatascience.com/how-to-build-a-market-simulator-using-markov-chains-and-python-7923256f8d29) - Modeling customer behavior!
 - [Building a Simple State Machine](https://dev.to/karn/building-a-simple-state-machine-in-python) - An article describing the importance of state, how it can be measured, and how to implement in Python.
 - [SimPy](https://simpy.readthedocs.io/en/latest/examples/index.html) - A simulation library built in python.
    - based on the ["SimPy in 10 Minutes"](https://simpy.readthedocs.io/en/latest/simpy_intro/process_interaction.html) article, I think it would even be possible to implement a version of this _without_ the use of a message-broker or queue system. I believe I could simply focus on using yielding functions and classes to manage this.
 - [Computational-Economy](https://github.com/uwol/computational-economy) - A github repo based off of [this paper (A Multi-Agent Non-Stochastic Economic
Simulator)](https://uwol.github.io/docs/2015-06_CEF2015-322.pdf).
 - [BashCafe](https://github.com/lucaswhitaker22/bash_cafe) - slightly different concept, but similar in nature! "The goal of the game is to predict how many coffees your need to make and how much to charge based off the temperature outside (since everyone loves an air conditioned cafe when its hot out). As the days progress, your goal is to make as much money as possible."
 - [StateMachine](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/StateMachine.html) - from the book, "Python 3 Patterns, Recipes, and Idioms", which talks about the management of state.
