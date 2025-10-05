import pandas as pd

df = pd.read_csv('./res/fake_restaurants_1000_expanded.csv')

df_drop = df.drop(columns=['id'])

def get_recommendations(cost, cuisine):

    df_copy = df_drop.copy(deep=True)

    # print(cost)
    # print(cuisine)
    # print(df_drop.to_string)

    # print("df copy v")
    # print(df_copy.to_string)
    for i in df_copy.index:
        if df_copy.loc[i, "avg_cost"] != cost or df_copy.loc[i, "cuisine"] not in cuisine:
            # print("drop")
            # print(df_copy.loc[i, "cuisine"])
            df_copy.drop(i, inplace=True)
    
    df_copy.sort_values('stars', ascending=False, inplace=True)
    
    reclist = []
    
    # print(len(df_copy['name']))
    for z in range(len(df_copy['name'])):
        row = []
        for x in range(4):
            if x == 1:
                row.append(float(df_copy.iloc[z, x]))
            else:
                row.append(df_copy.iloc[z, x])
        reclist.append(row)
     
    while len(reclist) > 10:
        reclist.pop(-1)

    return reclist

def get_recommendation_from_name(name):
    temp = []
    for i in df_drop.index:
        # print("before")
        # print(df_drop.to_string)
        # print(df_drop.loc[i, "name"])
        # print(name)

        if df_drop.loc[i, "name"] == name:
            # print("after")
            temp = get_recommendations(df_drop.loc[i, "avg_cost"], df_drop.loc[i, "cuisine"])
            break
        # print(df_drop.to_string)

    count = 0
    for x in temp:
        if temp[count][0] == name:
            temp.pop(count)
            break
        count += 1
    return temp

# test = get_recommendations('$$$$', ['Greek', 'Mediterranean','Indian'])    
# print(test)
# test2 = get_recommendation_from_name('Oasis Tapas Bar')
# print(test2)
# testfloat = float(test[0][1])
# print(testfloat)