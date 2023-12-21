import sys
from armpy.loader import ArmPy

sys.modules[__name__] = ArmPy('ru')
