usr=[{'name': 'aslam', 'id': 101, 'email': 'asd@', 'phoneno': 12345, 'password': 'asd123'}]
shop=[{'product': 'aaaa', 'id': 10, 'stock': 15, 'price': 1000},{'product': 'bbbb', 'id': 11, 'stock': 20, 'price': 1500}]
def register():
    if len(usr)==0:
        id=101
    else:
        id=usr[-1]['id']+1

    email=str(input('enter the email:'))
    f1=0
    for i in usr:
        if i['email']==email:                                                                           
            f1=1                                                                                   
            register()
    if f1==0:
        print('Registration')
        name=str(input('enter the name:'))
        phoneno=int(input('enter the phone no:'))
        password=str(input('enter the password:'))
        usr.append({'name':name,'id':id,'email':email,'phoneno':phoneno,'password':password})
def login():
    username=input('enter the uname:')
    password=input('enter the password:')
    f=0
    if username=='admin' and password=='admin':
        f=1
    user=''
    for i in usr:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    return f,user
def add_product():
    if len(shop)==0:
        id=10
    else:
        id=shop[-1]['id']+1

    f2=0
    for i in shop:
        if i['id']==id:                                                                           
            f2=1                                                                                   
            add_product()
    if f2==0:
        print('Product details')
        name=str(input('enter the product:'))
        stock=int(input('enter the stock:'))
        price=int(input('enter the price:'))
        shop.append({'name':name,'id':id,'stock':stock,'price':price})                                   
def view_product():                                                                                        
    for i in shop:
        print(i)
def update_product():
    id=int(input('enter the id:'))
    f2=0
    for i in shop:
        if i['id']==id:                                                                           
            f2=1                                                                                   
            stock=int(input('enter the stock:'))
            price=int(input('enter the price:'))
            i['stock']=stock
            i['price']=price
    if f2==0:
        print('invalid')
def delete_product():
    id=int(input('enter the id:'))
    f2=0
    for i in shop:
        if i['id']==id:                                                                           
            f2=1
            shop.remove(i)                                                                                   
    if f2==0:
        print('invalid')
def search_product():
    id=int(input('enter the id:'))
    f2=0
    for i in shop:
        if id==i['id']:
            print(i)
            f2=1
    if f==0:
        print('invalid id')
def view_user():
    for i in usr:
        print('USER')
        print('name:',i['name'])
        print('id:',i['id'])
        print('email:',i['email'])
        print('phoneno:',i['phoneno'])
def view_profile(user):
    print(user)
def update_profile(user):
    name=str(input('enter the name:'))
    phoneno=int(input('enter the phone no:'))
    user['name']=name
    user['phoneno']=phoneno
while True:
    print('''
    1.register
    2.login
    3.exit''')
    choice=int(input('enter the choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add products
                2.view products
                3.update product
                4.delete product
                5.search product 
                6.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    add_product()
                elif sub_choice==2:
                    view_product()
                elif sub_choice==3:
                    update_product()
                elif sub_choice==4:
                    delete_product()
                elif sub_choice==5:
                    search_product()
                elif sub_choice==6:
                    break

        elif f==2:
            while True:
                print('''
                1.view profile
                2.view product
                3.update profile
                4.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    view_profile(user)
                elif sub_choice==2:
                    view_product()
                elif sub_choice==3:
                    update_profile(user)
                elif sub_choice==4:
                    break
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid choice')