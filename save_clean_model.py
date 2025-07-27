from tensorflow.keras.models import load_model

# load original model
model = load_model("heart_mlp_model.h5", compile=False)

# save cleaned model
model.save("clean_heart_model.h5")
