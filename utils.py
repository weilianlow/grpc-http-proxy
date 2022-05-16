import os
from importlib.util import spec_from_file_location, module_from_spec
import inspect


class ProtoClassCollection:
    def __init__(self, root, suffix):
        self._dct = {}
        for subdir, dirs, files in os.walk(root):
            for f in files:
                mod_name = os.path.basename(f).split('.')[0]
                if f.endswith(suffix):
                    for key in self.inspect_module(mod_name, os.path.join(subdir, f)):
                        self._dct[key[0]] = key[1]

    def get_collection(self):
        return self._dct

    def get_stub_func(self, channel, cmd):
        stub_class = self._dct.get(cmd[0], None)
        stub = None
        if stub_class:
            stub_instance = stub_class(channel)
            stub = getattr(stub_instance, cmd[1])
        return stub

    @classmethod
    def inspect_module(cls, mod_name, full_path, predicate=inspect.isclass):
        lst = []
        spec = spec_from_file_location(mod_name, full_path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)
        for member in inspect.getmembers(mod, predicate):
            lst.append(member)
        return lst
