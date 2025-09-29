import pytest
from Common_Packages.Decorators.decorators import log_method, screenshot_on_assertion_failure

class Logmethodmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name, value in clsdict.items():
            if callable(value):
                # Apply logging decorator
                clsdict[name] = log_method(value, clsname)
                # Apply screenshot-on-assertion-failure decorator for test methods
                if name.startswith("test_"):
                    clsdict[name] = screenshot_on_assertion_failure(clsdict[name])

        new_cls = super().__new__(cls, clsname, bases, clsdict)

        # Optional: flaky retry
        if clsname.startswith('Test'):
            for name, value in new_cls.__dict__.items():
                if callable(value) and name.startswith('test_'):
                    setattr(new_cls, name, pytest.mark.flaky(reruns=0)(value))
        return new_cls
