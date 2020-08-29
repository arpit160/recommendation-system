import pandas as pd
# writing r is important
ratings= pd.read_csv(r"C:\Users\Arpit Singhal\Documents\moviedataset\ratings.csv")
movies=pd.read_csv(r"C:\Users\Arpit Singhal\Documents\moviedataset\movies.csv")
ratings=pd.merge(ratings,movies)

df=ratings.pivot_table(index='userId',columns='title',values='rating')
# droping all rows having na values more than 10
df=df.dropna(thresh=10,axis='columns')
df=df.fillna(0)

# calculating similarity matrix
# pearson method is also known as centered cosine similarity

similarity_df=df.corr(method='pearson')
print(similarity_df.head(30))
num =int(input("enter the number of movies u wnt to give"))

l=[]
for i in range(0,num):
    movie_name = input("enter a movie for which u want similar movies")
    rating_provided = int(input('enter rating given by u to above mentioned movie'))
    l.append((movie_name,rating_provided))

def get_movies(movie_name,rating_provided):
    r=similarity_df[movie_name]
    r=r*(rating_provided-2.5)
    #r=r.sort_values(ascending=False)
    return r
ans_df=pd.DataFrame()
for movie_name,rating_provided in l:
    p=get_movies(movie_name,rating_provided)
    ans_df=ans_df.append(p,ignore_index=True)



ans_df=ans_df.sum(axis='rows')
ans_df=ans_df.sort_values(ascending=False)
print(ans_df.head(20).index.tolist())


