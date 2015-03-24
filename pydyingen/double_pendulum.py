"""
This is an example of generation of double_pendulum on a higher level
"""
from multi_body_system import MultiBodySystem
from body import PyDyParticle

sys = MultiBodySystem('sys')
sys.gravity_vector = sys.root_frame.x

par1 = PyDyParticle('par1', sys.root_frame, 'q1', sys.root_frame.z)
par2 = PyDyParticle('par2', sys.root_frame, 'q2', sys.root_frame.z)

sys.add_body(par1)
sys.add_body(par2)

par1.set_ang_vel('u1', sys.root_frame, sys.root_frame.z, dynamic=True)
par2.set_ang_vel('u2', sys.root_frame, sys.root_frame.z, dynamic=True)

par1.set_point('l', sys.root_body.point, par1.frame.x)
par2.set_point('l', par1.point, par2.frame.x)

sys.root_body.connect_body(par1)
par1.connect_body(par2)

KM = sys.evaluate()
