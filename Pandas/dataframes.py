# pass in column names for each CSV
import pandas as pd
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv("/home/ramesh/Downloads/international-football-results-from-1872-to-2017.zip", sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv("/home/ramesh/Downloads/international-football-results-from-1872-to-2017.zip", sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')