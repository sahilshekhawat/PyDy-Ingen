from sympy import symbols
from sympy.physics.mechanics import dynamicsymbols
from sympy.physics.mechanics import Point, Particle
from sympy.physics.vector import ReferenceFrame


class Body(object):
    """
    TODO
    """

    def __init__(self, name):
        self.name = name
        self.frame = ReferenceFrame(name + '_frame')


class PyDyParticle(Body):
    """
    TODO
    """

    def __init__(self, name, ref_frame=None, angle=None, vector=None):
        Body.__init__(self, name)
        self.angle = angle
        self.mass = symbols(name + '_mass')
        self.point = Point(name + '_point')
        self.ref_frame = ref_frame
        self.name = self.name
        if ref_frame is not None:
            self.frame = ref_frame.orientnew(name + '_frame', 'Axis', [dynamicsymbols(angle), vector])
            self.q_ind = dynamicsymbols(angle)
            self.point.set_vel(self.frame, 0)
            self.point.set_vel(ref_frame, 0)
        else:
            self.frame = None
            self.q_ind = None
        self.body = Particle(name + '_body', self.point, self.mass)
        self.force = None
        self.u_ind = None

    def connect_body(self, body):
        # Right now, only works for particle-particle connections.
        body.point.v2pt_theory(self.point, self.frame, body.frame)

    def set_vel(self, value, frame, vector, dynamic=False):
        if dynamic:
            self.point.set_vel(frame, dynamicsymbols(value) * vector)
        else:
            self.point.set_vel(frame, symbols(value) * vector)

    def set_ang_vel(self, value, frame, vector, dynamic=False):
        if dynamic:
            self.u_ind = dynamicsymbols(value)
            self.frame.set_ang_vel(frame, self.u_ind * vector)
        else:
            self.u_ind = symbols(value)
            self.frame.set_ang_vel(frame, symbols(value) * vector)

    def set_force(self, value, vector):
        self.force = (self.point, value * vector)

    def set_point(self, distance, ref_point, vector):
        self.point = ref_point.locatenew(self.name + '_point', dynamicsymbols(distance) * vector)
        self.point.set_vel(self.ref_frame, 0)
        self.point.set_vel(self.frame, 0)

class PyDyRigidBody(Body):
    """
    TODO
    """
