"""
Practicing COMPOSITION - building up classes by passing other instances of classes
"""
import math


class Tire:
    """
  Tire represents a tire that would be used with an automobile.
  """

    def __init__(self, tire_type, width, ratio, diameter, brand="", construction="R"):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumference(self):
        """The circumference of the tire in inches
        Run below command to run below doctest in REPL
        python3 -m doctest -v tire.py 
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        # alternatively, you could remove the side_wall_inches variable and line, and simply set
        # total_diameter to the below, which calls on the below _side_wall_inches method:
        # total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        """
      Represents the tire's information in the standard notation present
      on the side of the tire. Example: 'P215/65R15'
      When we print it out, it will print out the below representation
      """
        return (
            f"{self.tire_type}{self.width}/{self.ratio}"
            + f"{self.construction}{self.diameter}"
        )

    # set base calculation to measure circumference in below SnowTire class
    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4


# create another class, treating Tire as super class
class SnowTire(Tire):
    # redefine init to add in chain thickness
    def __init__(
        self,
        tire_type,
        width,
        ratio,
        diameter,
        chain_thickness,
        brand="",
        construction="R",
    ):
        # pass in Tire's init first so we don't have to set duplicate info again
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    # now we need to override the circumference method due to our added chain
    def circumference(self):
        """
      The circumference of a tire w/ snow chains in inches.

      >>> tire = SnowTire('P', 205,65,15,2)
      >>> tire.circumference()
      92.7
      """
        total_diameter = (
            self._side_wall_inches() + self.chain_thickness
        ) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    # call on repr to designate that we are a snow tire
    def __repr__(self):
        return super().__repr__() + " (Snow)"
