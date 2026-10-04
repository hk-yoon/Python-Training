import pickle

data = {"gene": "TP53", "score": 0.92}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
with open("data.pkl", "rb") as f:
    print(pickle.load(f))
print("Never load an untrusted pickle file blindly.")
