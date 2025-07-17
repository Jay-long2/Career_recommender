import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv("/home/jlong/Desktop/career recommender system/career_recommender/Data_final (2).csv")

# Separate features and target
X = df.drop(columns=["Career"])
y = df["Career"]

# Encode the target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X, y_encoded)

# Save the model and encoder
joblib.dump(model, "/home/jlong/Desktop/career recommender system/career_recommender/career_model.pkl")
joblib.dump(target_encoder, "/home/jlong/Desktop/career recommender system/career_recommender/career_target_encoder.pkl")

"/home/jlong/Desktop/career recommender system/career_recommender/career_model.pkl", "/home/jlong/Desktop/career recommender system/career_recommender/career_target_encoder.pkl"