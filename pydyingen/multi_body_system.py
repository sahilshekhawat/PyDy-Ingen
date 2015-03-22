from sympy import symbols

from sympy.physics.mechanics import functions
from sympy.physics.mechanics import dynamicsymbols
from sympy.physics.mechanics import Point, ReferenceFrame, RigidBody
from sympy.physics.mechanics import KanesMethod

from body import PyDyParticle


__all__ = ['MultiBodySystem']


class MultiBodySystem(object):
    """
    TODO
    """

    def __init__(self, name):
        self.name = name
        self.root_frame = ReferenceFrame('N')  # Raise error that 'N' is taken.
        self.origin = Point('O')  # Raise error that 'O' is taken.
        self.origin.set_vel(self.root_frame, 0)
        self.root_body = PyDyParticle(name, )
        self.body_list = list()
        self.force_list = None
        self.q_ind = Non
        self.u_ind = None
        self.gravity_vector = None

    def set_gravity_vector(self, gravity_vector):
        self.gravity_vector = gravity_vector

    def get_gravity_vector(self):
        return self.gravity_vector

    gravity_vector = property(get_gravity_vector, set_gravity_vector)

    def add_body(self, body):
        self.body_list.append(body)

    def evaluate(self):
        self.force_list = list()
        self.u_ind = list()
        self.q_ind = list()
        kd = list()
        for body in self.body_list:
            body_kd = dynamicsymbols(body.angle, 1)
            kd.append(body_kd - body.u_ind)
            if self.gravity_vector:
                m, g = symbols('m g')
                self.force_list.append(m * g * self.gravity_vector)
            else:
                if body.force:
                    self.force_list.append(body.force)
            self.u_ind.append(body.u_ind)
            self.q_ind.append(body.q_ind)

        km = KanesMethod(self.root_frame, q_ind=self.q_ind, u_ind=self.u_ind, kd_eqs=kd)
        return km.kanes_equations(self.force_list, self.body_list)
