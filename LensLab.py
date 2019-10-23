from sympy import Eq, solve, subs, symbols

class Application():
    """
    Description: User defines what they are tring to do, i.e. lens design, interferograms, etc.

    Notes:
    """
    def __init__(self,type):
        self.type = type
        print("Booting Pyght")

class System():
    """
    Description: Defines everything about the optical system as a whole, i.e. environment

    Notes:
    """
    def __init__(self):
        print("New system created")
    
    def addSurf(self):
        """
        Description: Adds a new surface into the system

        Notes:
        """
        new_surf = Surf()
        self.Surfs.append(new_surf)

    def addRay(self, wl, h):
        """
        Description:Adds a new ray, with inputs of wavelength and field height

        Notes:
        """

        new_ray = Ray()
        self.Rays.append(new_ray)

class Ray():
    """
    Description: Defines rays through the system

    Notes:
    """
    def __init__(self, wl, h):
        Ray.wl = wl
        Ray.h = h

    def trace(self,x0,y0,z0,xd,yd,zd): 
        """
        Description: Traces ray through system, x0, y0, z0 are ray launch coords and xd, yd, zd are components of the unit vector direction of the ray
        
        Notes:
        """
        t = symbols('t')
        #find intersection points for each surface and take the one it hits first
        # I want to make this fairly non sequential. All rays get traced to each surface. not sure how this is gonna go yet
        for element in self.Elements:
            for surface in element.surface:
                intersect = self.equation.subs(x,x0+t*xd).subs(y,y0+t*yd).subs(z,z0+t*zd)
                pathlength = solve(intersect,t) ###spits out path length from launch location to surface intersection
                #More stuff to find the XYZ coordinates of intersection, make sure that location is within the specified aperture etc
                # then do refraction/reflection stuff

class Surf():
    """
    Description: Surfaces in the system

    Notes:
    """
    def __init__(self, type):
        Surf.type = type

    def defineRefr(self):
        """
        Description: Define properties of a refractive surface

        Notes:
        """
        self.shapetype = input()
        if self.shapetype == 'Paraxial':
            self.thickness = 0
            self.focal_length = input()
            self.semi_diameter = input()
            self.material = input()
            self.equation = self.setupSurf('Paraxial')

        elif self.shapetype == 'Spherical':
            self.equation = self.setupSurf('Sphereical')

    def setupSurf(self):
        """
        Description: Sets up the equation of the surface

        Notes:
        """
        if self.shapetype == 'Paraxial':

        elif self.shapetype == 'Flat':
            A,B,C,D,x,y,z = symbols('A B C D x y z')

            self.equation = Eq(A*x+B*y+C*Z+D)

        elif self.shapetype == 'Spherical':
            x,y,z,x_s,y_s,z_s,R = symbols('x y z x_s y_s z_s R') #underscore s is the shift
            self.equation = Eq((x-x_s)**2+(y-y_s)**2+(z-z_s)**2-R**2)
        else:
            print('Invalid Surface Shape type')
            return



#   Ok. Element class. When you want to insert a new element (called from the System class),
#   you'll be able to select what type of element you want(lens mirror prism etc), then select material,
#   surface coatings, semi diameter, center thickness etc
#   Another nice thing I really want is to be able to look at the new element you're creating
#   by itself before inserting it into the whole system. Also since they are now specified as elements,
#   they can be more easily flipped
class Element():
    def __init__(self, type)
        self.type = type
        if self.type == "Refractive:
            self.surface[0] = Surface('Refr')
            self.surface[1] - Surface('Refr')

        if self.type == "Reflective"
            self.surface = Surface('Refl')