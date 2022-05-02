my_list = (12, 12.5, True, 'hello', [1, 2], {1, 2}, {1: 2, 5: 7}, None, (1, 2), frozenset(), range(2), b'twelve',
           bytearray(b'thirteen'), TypeError, zip(*[(14, 15), (16, 17)]))

for i, item in enumerate(my_list, 1):
    print(f'{i}. {item} -> {type(item)}')
