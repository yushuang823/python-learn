if __name__ == '__main__':
    def my_abs(x):
        if not isinstance(x,(int,float)):
            raise TypeError('type error')
        if x > 0:
            return x
        else:
            return -x
    print(my_abs(-9))
    print(my_abs(-3))