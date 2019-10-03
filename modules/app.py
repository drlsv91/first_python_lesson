# MODULES
# a module is a file that contain some python code
# from sales import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()
# # OR
# sales.calc_tax()
# sales.calc_shipping()

# COMPILED PYTHON FILES
# MODULE SEARCH PATH
# import sales
# import sys
# print(sys.path)

# calc_tax()
# OR
# PACKAGES
# from ecommerce import sales
# from ecommerce.sales import calc_tax
# sales.calc_tax()

# SUB-PACKAGES
# from ecommerce.shopping import sales
# from ecommerce.shopping.sales import calc_tax
# sales.calc_tax()

# INTRA-PACKAGE REFRENCES
# relative import vs absolute import

# THE DIR() FUNCTION
from ecommerce.shopping import sales

print(dir(sales))  # useful for debugging


# EXECUTING MODULES AS SCRIPT
