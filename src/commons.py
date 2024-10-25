import numpy as np


def convert_to_ascii(input_data: str):
    """String to ASCII converter"""
    input_data_to_char = []
    for i in input_data:
        input_data_to_char.append(ord(i))
    Zero_array = np.zeros((400))
    indexs = min(len(input_data_to_char), 400)
    for i in range(indexs):
        Zero_array[i] = input_data_to_char[i]
    Zero_array.shape = (20, 20)
    return Zero_array
