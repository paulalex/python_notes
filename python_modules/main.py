import sys
import os
sys.path.append("/Users/paoc/PycharmProjects/edureka_python_course/python_modules/python_package/module_one")
sys.path.append("/Users/paoc/PycharmProjects/edureka_python_course/python_modules/python_package/module_two")

import module_one_script as func

if __name__ == "__main__":
    func.function_module_one()
    print(eval("25 * 10"))
    print(sys.path)

    new_path = os.path.join(os.path.abspath("."), "hello/world")
    print(os.path.abspath("."))
    print(new_path)
    print(os.listdir("."))
