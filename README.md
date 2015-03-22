#### Follows is double pendulum example as in pydy/examples/double_pendulum/double_pendulum.py

from pydyingen import PyDyParticle, MultiBodySystem

sys = MultiBodySystem('sys')
sys.gravity_vector = sys.root_frame.x

par1 = PyDyParticle('par1', sys.root_frame, 'q1', sys.root_frame.z)
par2 = PyDyParticle('par2', sys.root_frame, 'q2', sys.root_frame.z)


sys.add_body(par1)
sys.add_body(par2)

par1.set_point('l', sys.origin, par1.frame.x)
par2.set_point('l', par1.point, par2.frame.x)

par1.set_ang_vel('u1', sys.root_frame, sys.root_frame.z, dynamic=True)
par2.set_ang_vel('u2', sys.root_frame, sys.root_frame.z, dynamic=True)

kanes_equations = sys.evaluate()

