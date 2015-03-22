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
        self.root_body = PyDyParticle(name)
        self.root_body.point.set_vel(self.root_frame, 0)
        self.root_body.frame = self.root_frame
        self.body_list = list()
        self.force_list = None
        self.q_ind = None
        self.u_ind = None
        self.gravity_vector = None
        self.body_body_list = list()

    def add_body(self, body):
        self.body_list.append(body)
        self.body_body_list.append(body.body)

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
                self.force_list.append((body.point, m * g * self.gravity_vector))
            else:
                if body.force:
                    self.force_list.append(body.force)
            self.u_ind.append(body.u_ind)
            self.q_ind.append(body.q_ind)

        # print "q_ind: " + str(self.q_ind)
        # print "u_ind: " + str(self.u_ind)
        # print "kd: " + str(kd)
        # print "body_body_list: " + str(self.body_body_list)
        # print "force_list: " + str(self.force_list)
        km = KanesMethod(self.root_frame, q_ind=self.q_ind, u_ind=self.u_ind, kd_eqs=kd)
        return km.kanes_equations(self.force_list, self.body_body_list)
