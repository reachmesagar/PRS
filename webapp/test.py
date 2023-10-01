from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Sample data: user ID, item ID, and ratings
data = [
    ('user1', 'item1', 5),
    ('user1', 'item2', 4),
    ('user2', 'item1', 3),
    ('user2', 'item2', 2),
    ('user3', 'item2', 4),
    ('user3', 'item3', 5),
]

# Create a DataFrame from the data
reader = Reader(line_format='user item rating', sep=',')
dataset = Dataset.load_from_df(pd.DataFrame(data, columns=['user', 'item', 'rating']), reader)

# Split the dataset into train and test sets
trainset, testset = train_test_split(dataset, test_size=0.2)

# Use KNNBasic algorithm for collaborative filtering
sim_options = {'name': 'cosine', 'user_based': True}
algo = KNNBasic(sim_options=sim_options)

# Train the algorithm on the training set
algo.fit(trainset)

# Predict ratings for the test set
predictions = algo.test(testset)

# Calculate and print RMSE (Root Mean Squared Error)
rmse = accuracy.rmse(predictions)
print(f'RMSE: {rmse}')
