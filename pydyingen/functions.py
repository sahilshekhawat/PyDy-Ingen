import abc

from sympy import symbols
from sympy.physics.mechanics import dynamicsymbols
from sympy.physics.mechanics import functions
from sympy.physics.mechanics import Point, ReferenceFrame, RigidBody
from sympy.physics.mechanics import KanesMethod


class Rotate(object):
    """TODO"""

    def __init__(self, angle, ref_frame, frame, vector, dynamic=False, ):
        self.vector = vector
        self.frame = frame
        if dynamic:
            self.angle = dynamicsymbols(angle)
        else:
            self.angle = symbols(angle)
        frame.set_ang_vel(ref_frame, self.angle * vector)



class Translate(object):
    """TODO"""

    def __init__(self, distance, body, ref_point, vector, dynamic=False):
        if dynamic:
            self.distance = dynamicsymbols(distance)
        else:
            self.distance = symbols(distance)
        body.point = ref_point.locate_new(body.name + '_point', self.distance * vector)
