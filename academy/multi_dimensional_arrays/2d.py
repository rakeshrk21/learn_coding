def iter_2d_array(arr):

    for row in arr:
        for val in row:
            print(val)

def iter_3d_array(arr):

    for row in arr:
        for val in row:
            for item in val:
                print(item)


if __name__ == "__main__":
    arr2d = [
        [1,9,78], [4, 5, 9]
    ]
    # iter_2d_array(arr2d)

    arr3d = [
       [ [5, 4, 3], [1, 9, 78] ],
       [ [7, 9, 8], [4, 3, 21] ],
    ]

    iter_3d_array(arr3d)