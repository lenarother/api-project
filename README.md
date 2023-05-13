# Entity-control-boundary pattern

Also called BCE (boundery-controll-entity)


Goal:
* separates the business domain from the rest of the world
* one can see what the application does on the first glance 


Each package has module:
* boundary
* entity
* controller


Boundary:
* contains public api
* module code should be used only through these functions
* api endpoint is also a boundary
* strictly defined input / output (boundary objects e.g. as request / response objects) and does validation so that incorrect objects does not make it into controller (e.d. done with pydantic)
* boundary object does nothing is just for transferring data. If methods are added separation is lost.
* contract: you give boundary input object and get boundary output object or an error


Controller:
* implements a use case (an interaction between a system and its users, work that needs to be done, could be done on a paper without computer)
* does the work
* boundary calls controller
* receipts how to perform use cases (calculate things)
* the only place that does things
* can be split into multiple files, one main controller file that keeps public functions for the boundary.
* can talk to multiple boundaries


Entity:
* by the book - core business objects
* interesting part:
  * what with the things that are common across the project e.g. country codes -> use independent layer outside bce pattern.
  * why: this parts does not make sense as bce, as it would dilute the core functionality  


Testing:
* test boundaries
* test business entities 


Refactoring:
* elephant carpaccio 
* refactoring into bce can be done in small steps
* place to store non key functional services


Resources:
* https://www.feststelltaste.de/uncle-bob-explains-the-boundary-control-entity-pattern-in-detail/