from sympy import Eq, solve, subs, symbols


# Alight so here's the dealio so far. I'm trying to lay out the framework for
#   all the object classes (See descriptions next to each one for what I'm
#   thinking it will contain)

#   I'm thinking this class is like the master it will have all the UI control
#   in it and will probably end up closely involving the System class. I don't
#   really know what to do with it yet but I'm not gonna mess with it for awhile.
#   @Scott might be something you'd be really good at
class Application():
    def __init__(self):
        print("Booting LensLab")

#   The system class defines everything about the optical system as a whole
#   It contains all of the elements and where they are, information about the
#   environment(temp/pressure), wavelength, shit like that. It'll have a bunch
#   of methods for insterting elements, and basically just adjusting all of the
#   described above
class System():
    def __init__(Self):
        #sfvnef
        def insertElement(self):
            type = input('What type of element (Relfective or Refractive)')
            new_element = Element(type)
            self.Elements.append(new_element)
        #I actually think I want to make a Ray class from the below stuff
        def TraceRay(self,x0,y0,z0,xd,yd,zd): #x0,y0,z0 are ray launch coords and xd,yd,zd are components of the unit vector direction of the ray
            t = symbols('t')
            #find intersection points for each surface and take the one it hits first
            # I want to make this fairly non sequential. All rays get traced to each surface. not sure how this is gonna go yet
            for element in self.Elements:
                for surface in element.surface:
                    intersect = self.equation.subs(x,x0+t*xd).subs(y,y0+t*yd).subs(z,z0+t*zd)
                    pathlength = solve(intersect,t) ###spits out path length from launch location to surface intersection
                    #More stuff to find the XYZ coordinates of intersection, make sure that location is within the specified aperture etc
                    # then do refraction/reflection stuff

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

#   Surface class is for defining surfaces of your element, again as either reflective or Refractive
#   It also sets up the shape of the surface in the form of an equation
#   so surface.equation always contains the symbolic equation to that surface
class Surface():
    def __init__(self, type):
        Surface.type = type
        if Surface.type  == 'Refl':
            self.setuprefl()
        elif Surface.type  == 'Refr':
            self.setuprefr()


    def setuprefr(self):
        self.shapetype = input()
        if self.shapetype == 'Paraxial':
            self.thickness = 0
            self.focal_length = input()
            self.semi_diameter = input()
            self.material = input()
            self.equation = self.setup_equation('Paraxial')

        elif self.shapetype == 'Spherical':

    def setup_equation(self):
        #More types of surfaces to be added later
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
