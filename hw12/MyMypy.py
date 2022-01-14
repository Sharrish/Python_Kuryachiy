"""

https://uneex.org/LecturesCMC/PythonIntro2021/Homework_MyMypy

"""



from inspect import getfullargspec


class checked(type):
    def __new__(mcs, name, parents, ns):
        def decorator(method):
            def check_types(*args, **kwargs):
                method_info = getfullargspec(method)

                def real_args():
                    for i in range(min(len(args), len(method_info.args))):
                        if method_info.args[i] in method_info.annotations:
                            if not isinstance(args[i], method_info.annotations[method_info.args[i]]):
                                raise TypeError(f"Type mismatch: {method_info.args[i]}")

                def missed_args():
                    for i in range(min(len(args), len(method_info.args)), len(args)):
                        if not isinstance(args[i], method_info.annotations[method_info.varargs]):
                            raise TypeError(f"Type mismatch: {method_info.varargs}")

                def check_kwargs():
                    for kwarg in kwargs:
                        type_check = None
                        if kwarg in method_info.annotations:
                            type_check = method_info.annotations[kwarg]
                        elif method_info.varkw in method_info.annotations and kwarg not in (method_info.kwonlyargs +
                                                                                            method_info.args):
                            type_check = method_info.annotations[method_info.varkw]
                        if type_check and not isinstance(kwargs[kwarg], type_check):
                            raise TypeError(f"Type mismatch: {kwarg}")

                def check_ret(r):
                    if not isinstance(r, method_info.annotations["return"]):
                        raise TypeError("Type mismatch: return")

                real_args()
                if method_info.varargs in method_info.annotations:
                    missed_args()
                check_kwargs()
                ret = method(*args, **kwargs)
                if "return" in method_info.annotations:
                    check_ret(ret)
                return ret
            return check_types

        nns = {n: decorator(f) for n, f in ns.items() if callable(f) and not n.startswith("__")}
        ns.update(**nns)

        return super().__new__(mcs, name, parents, ns)