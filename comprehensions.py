def run():
    list={}
    for i in range(1,101):
        if i%3!=0:
            list[i]=i**3
    print(list)

    dict={i: pow(i,2) for i in range(1,1001)}
    print(dict)


if __name__=='__main__':
    run()