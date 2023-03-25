"""
tpl_comp = (num * 10 for num in range(5))
print(tpl_comp)
print(tpl_comp)<generator object <genexpr> at 0x0000012ACA468040>
"""

tpl_comp = *(num * 10 for num in range(5)),
print(tpl_comp)

tpl_comp_N = tuple(num * 10 for num in range(5+1))
print(tpl_comp_N)