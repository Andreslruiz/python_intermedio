def run():
    my_list=[1,"Hello",True, 4.5]
    my_dict={'Firstname': 'Andres', 'Lastname':'Loaiza'}
    superlist=[
        {'Firstname': 'Andres', 'Lastname':'Loaiza'},
        {'Firstname': 'Carlos', 'Lastname':'Ruiz'},
        {'Firstname': 'Daniel', 'Lastname':'Garcia'},
        {'Firstname': 'David', 'Lastname':'Medina'},
    ]

    superdict={
        'natural_nums':[1,2,3,4,5],
        'integer_nums':[-2, -1, 0, 1, 2],
        'floating_nums':[1.1, 4.5, 6.43]
    }

    for value in superlist:
        print('-- ', value)


if __name__=='__main__':
    run()