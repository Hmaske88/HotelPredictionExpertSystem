import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from csv import writer

df=pd.read_csv("RestoInfo2.csv")

#d={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I'}
d={0:'The Cafe Terrace',1:'The Cherry Blossom',2:'The Cutting Board',3:'The Diamond',4:'The Golden Fork',5:'The Green Plate',6:'The Chef’s Table',7:'The Bell Tower',8:'The Brick Oven'}

df2=df.copy()

le=LabelEncoder()
df2['area']=le.fit_transform(df2['area'])
df2['food']=le.fit_transform(df2['food'])
df2['food type']=le.fit_transform(df2['food type'])
df2['discount']=le.fit_transform(df2['discount'])
df2['restaurant']=le.fit_transform(df2['restaurant'])

x=df2[['area','rent','stars','food','food type','discount']]
y=df2['restaurant']

encode = LabelEncoder()
y = encode.fit_transform(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.02,random_state = 0)

naive_bayes = GaussianNB()
naive_bayes.fit(x_train,y_train)
pred = naive_bayes.predict(x_test)

def add():
    area=input("pune/mumbai :")
    rent=int(input("Expected Room Rent :"))
    stars=int(input('Stars (1/2/3/4/5) :'))
    food=input("Food (low/average/expensive) :")
    food_type=input("Food Type (veg/non-veg) :")
    discount=input("Discount (yes/no) :")
    List=[area,rent,stars,food,food_type,discount]
    with open('input.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

def predict():
    new_data=pd.read_csv("input.csv")
    new2=new_data.copy()
    le=LabelEncoder()
    new2['area']=le.fit_transform(new2['area'])
    new2['food']=le.fit_transform(new2['food'])
    new2['food type']=le.fit_transform(new2['food type'])
    new2['discount']=le.fit_transform(new2['discount'])
    predictions = naive_bayes.predict(new2)
    print("\nHotel : ",d[predictions[0]])
    new_data = new_data.iloc[:-1]
    new_data.to_csv('input.csv', index=False)

add()
predict()