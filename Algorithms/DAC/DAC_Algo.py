def DAC_max(a, index, l):
    max = -1

    if index >= l-2:
        if a[index] > a[index+1]:
            return a[index]
        else:
            return a[index+1]
    max = DAC_max(a, index+1, l)
    # print(index)
    # print(max)

    if a[index] > max:
        return a[index]
    else:
        return max


if __name__ == '__main__':
    # min,max = 0,-1

    a = [70, 250, 50, 80, 140, 12, 14]

    # Recursion - DAC_Max function called
    max = DAC_max(a, 0, 7)

    print('max number', max)
