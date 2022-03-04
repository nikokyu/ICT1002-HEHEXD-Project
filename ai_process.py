# csv to ai model to predict results (attack type)
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def predict(filepath):
    test_dataset = pd.read_csv(filepath, low_memory=False)
    test_features = test_dataset[["TTL", "window size", "tcp flag", "ct_srv_dst", "ct_src_ltm", "ct_dst_sport_ltm"]].values
    #test_features = test_dataset.iloc[:, [9,10,18,19,27,33,36,41,43,45]].values

    # Feature Scaling
    sc = StandardScaler()
    sc.fit(test_features)
    test_features = sc.transform(test_features)
    classifier = pickle.load(open("ai/model.pickle", 'rb'))
    test_pred = classifier.predict(test_features)
    test_dataset = test_dataset[["srcip", "sport", "dstip", "dport", "TTL", "window size", "tcp flag", "ct_srv_dst", "ct_src_ltm", "ct_dst_sport_ltm"]]
    test_dataset['attackcat'] = test_pred.tolist()

    return test_dataset
