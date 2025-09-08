import pandas as pd  # Importing the pandas module as pd
df_Squrrel = pd.read_csv("Squirrel-Data.csv")  # Reading the Squirrel-Data.csv file into a dataframe called df_Squrrel

colors_list = df_Squrrel["Primary_Fur_Color"].to_list()  # Converting the Primary_Fur_Color series to a list (colors_list)
color_set = set(colors_list)   # Converting colors_list to a set of unique colors called color_set

Squrrel_count = {  # Dictionary to contain unique colors and their total occurrences
    "fur_color" : [],
    "count" : []
}

for unique_color in color_set:   # Initializing the for loop to iterate through color_set 
    if type(unique_color) == type('string'): # Adding type checking to process only string datatypes
        count = colors_list.count(unique_color)  # Counting the occurrences of a unique color in colors_list and storing in the count variable
        Squrrel_count["fur_color"].append(unique_color)  # Appending unique_color to the fur_color list in the Squrrel_count dictionary
        Squrrel_count["count"].append(count) # Appending the occurrence count to the count list in the Squrrel_count dictionary

df_Squrrel_count = pd.DataFrame(Squrrel_count)   # Converting the dictionary into a dataframe df_Squrrel_count
df_Squrrel_count.to_csv("Squirell_count.csv")   # Saving the df_Squrrel_count dataframe as a CSV file named Squirell_count.csv