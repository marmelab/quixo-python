cross_raw = '''\
 ____________
|   __  __   |
|   \ \/ /   |
|    \  /    |
|    /  \    |
|   /_/\_\   |
|____________|
'''

cross = [[char for char in row] for row in cross_raw.split('\n')]

cicle_raw = '''\
 ____________
|            |
|    .--.    |
|   /    \   |
|   \    /   |
|    '--'    |
|____________|
'''
circle = [[char for char in row] for row in cicle_raw.split('\n')]

empty_raw = '''\
 ____________
|            |
|            |
|            |
|            |
|            |
|____________|
'''
empty = [[char for char in row] for row in empty_raw.split('\n')]
