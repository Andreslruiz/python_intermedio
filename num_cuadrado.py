def run():
    # list=[]
    # for i in range(1,101):
    #     if i%3!=0:
    #         list.append(i**2)
    # print(list)
    list=[i for i in range(1,9999) if i%36!=0]
    print(list)





if __name__=='__main__':
    run()