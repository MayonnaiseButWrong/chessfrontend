from translations import *

temp = [['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ['WP','WP','WP','WP','WP','WP','WP','WP'],
 ]
xen = to_xenonnumber(temp)
print(xen)
g = to_gamelist(str(xen))
print(g)