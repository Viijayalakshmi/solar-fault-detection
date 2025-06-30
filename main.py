import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load trained model
model = load_model('models/solar_fault_detector.h5')

def predict_solar_fault(image_path):
    img = load_img(image_path, target_size=(32, 32))  # ✅ Fixed size
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)[0]
    label = "Faulty" if prediction[0] > prediction[1] else "Normal"

    print(f"✅ Prediction: {label}")
    plt.imshow(img)
    plt.axis('off')
    plt.title(label)
    plt.show()

# Run prediction on sample image
predict_solar_fault("test_images/sample.jpg")
