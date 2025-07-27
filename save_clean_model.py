from tensorflow.keras.models import load_model

# load the original model
model = load_model("heart_mlp_model.h5")

# save it in the recommended format
model.save("clean_heart_model.keras")