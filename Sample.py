import random

def main():
    min_str = '-0.1'
    max_str = '0.1'

    min_digit_num = len(min_str.split('.')[1])
    max_digit_num = len(max_str.split('.')[1])

    digit_num = min_digit_num if min_digit_num > max_digit_num else max_digit_num

    min = float(min_str)
    max = float(max_str)
    for index in range(digit_num):
        min *= 10
        max *= 10
    min_i = int(min)
    max_i = int(max)
    print(min_i, max_i)
    v = random.sample(range(min_i, max_i), k=3)
#    for index in range(digit_num):
#        min /= 10
#        print(min)
#    form = '{:.' + str(digit_num) +'f}'
#    t_min = form.format(min)

#    print('{}'.format(v))

if __name__ == '__main__':
    main()
