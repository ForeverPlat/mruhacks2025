import pandas as pd

df = pd.read_csv('./res/fake_restaurants_1000_expanded.csv')

df_drop = df.drop(columns=['id'])

def get_recommendations(cost, cuisine):

    for i in df_drop.index:
        if df_drop.loc[i, "avg_cost"] != cost or df_drop.loc[i, "cuisine"] != cuisine:
            df_drop.drop(i, inplace=True)
    
    df_drop.sort_values('stars', ascending=False, inplace=True)
    
    reclist = []
    
    for z in range(len(df_drop['name'])):
        row = []
        for x in range(4):
            if x == 1:
                row.append(float(df_drop.iloc[z, x]))
            else:
                row.append(df_drop.iloc[z, x])
        reclist.append(row)
     
    while len(reclist) > 10:
        reclist.pop(-1)

    return reclist

def get_recommendation_from_name(name):
     for i in df_drop.index:
         if df_drop.loc[i, "name"] == name:
             temp = get_recommendations(df_drop.loc[i, "avg_cost"], df_drop.loc[i, "cuisine"])
             break
     count = 0
     for x in temp:
         if temp[count][0] == name:
             temp.pop(count)
             break
         count += 1
     return temp

# test = get_recommendations('$', 'BBQ')    
# print(test)
# test2 = get_recommendation_from_name('Oasis Tapas Bar')
# print(test2)
# testfloat = float(test[0][1])
# print(testfloat)