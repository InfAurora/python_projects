def main():
    nums1 = [1, 90, -33, -55, 67, -16, 28, -55, 15]
    nums2 = [999, -60, -77, 14, 160, 301]
    nums3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 
140, 150, 160, 170, 180, 190, 200, -99]
    print(arrayAdder(nums1))
    print(arrayAdder(nums2))
    print(arrayAdder(nums3))

def arrayAdder(array):
    total = 0
    for i in array:
        total += i
    return total


if __name__ == "__main__":
    main()