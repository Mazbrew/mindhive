import pandas as pd
import string

if __name__ == "__main__":
    #opening the file, reading its contents and putting it into a dataframe
    df = pd.read_csv("dataset-ori.csv").set_index("Product ID")

    #category can be filled in based on description/product name
    #   methods to deal with missing values is to:
    #       delete data row/ column(case by case)
    #       use some sort of machine learning method to find the value that fits best(better for large datasets)
    #       use context clues to fill it in manually (for this small dataset i presumed this was the best method)
    df.at[30,"Category"] = "Home & Kitchen"
    df.at[36,"Category"] = "Arts & Crafts"
    df.at[40,"Category"] = "Electronics"

    #products with no Product Name and description were deleted
    #no way to predict the kind of item the "shop" is selling, not enough data
    #should not fill in data willy nilly
    df = df.dropna(how = "all",subset = ["Product Name", "Description"], axis= 0)
    
    #for the prices, i got the average price of the items on shopee
    #   though in this situation it would be better to request the pricing from the client, 
    #   for the sake of having more data, I got the average prices of matching items on shopee
    #   the prices are then rounded up to the closes 0.99
    df.at[29,"Price"] = "2.99"
    df.at[31,"Price"] = "70.99"
    df.at[34,"Price"] = "130.99"
    df.at[37,"Price"] = "31.99"

    print(df)

    #for the missing description, i got the description of a matching item on shopee
    #   yet again for this it's better to request the data from client
    #   for the sake of having more data it was filled in anyway
    #   ensuring that there are no more than 3 descriptors to match the rest of the dataset
    df.at[28,"Description"] = "Fluorescent numbers, Non-Ticking"
    df.at[33,"Description"] = "The Little Prince, The Old Man and The Sea, Animal Farm"

    #images for all the items in question are available in the images folder

    #Unsure if the letters that came along with the Product Name are the "brand names"
    #   they have been removed so that it can be displayed on the frontend easier without the need for the backend to process it
    for i in range(len(df)):
        temp = df.iloc[i]["Product Name"]
        df.iat[i,0] = temp.rsplit(' ', 1)[0]

    #removal of extra "," at the end of description for sandals and aluminium bike
    df.at[27,"Description"] = "21-speed, Aluminum frame"
    df.at[35,"Description"] = "Leather, Size 7"

    #Capitalized first letter of every word after ", "
    for i in range(len(df)):
        temp = df.iloc[i]["Description"]
        df.iat[i,1] = string.capwords(temp, sep =", ")

    df.to_csv("dataset-preprocessed.csv", encoding="utf-8")


    

