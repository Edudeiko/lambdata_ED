"""
train, val, test split. 20% for the test data set
"""
from sklearn.model_selection import train_test_split


def t_v_t_split(_):

    train, test = train_test_split(_, train_size=0.8)
    train, val = train_test_split(train, train_size=0.8)

    return train, val, test
