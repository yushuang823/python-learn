if __name__ == '__main__':
    def power(x,n):
        s = 1
        while n > 0:
            n = n -1
            s = s * x
        return(s)
print(power(2,3))
print(power(2,4))
print(power(5,2))