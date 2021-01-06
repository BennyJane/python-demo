from class_super_type_object.global_func import name, global_params
from class_super_type_object.global_func import f


# print(global_params.get("__name__"))

# print(f()[0], "this is a function ")


# print(global_params.get("__name__"))

def func():
    res = global_params.get("__name__")
    print("func ...", res)
    return res


func()
