import os
import matplotlib.pyplot as plt
import tensorflow as tf

def plot_history(model_history, seq_1, seq_2):
    plt.plot(model_history.history[seq_1], label=seq_1)
    plt.plot(model_history.history[seq_2], label=seq_2)
    plt.legend()
    plt.title("training history");

def load_model(fpath, optimizer=None, loss=None, isCompile=False):
    
    model = tf.keras.models.load_model(fpath, compile=isCompile)
    
    if not isCompile:
        model.compile(
            optimizer=optimizer,
            loss=loss,
            metrics=["accuracy"]
        )
    
    return model

# Preprocess Data
def preprocess_img(img, width, height):
    img = tf.io.read_file(img)
    img = tf.io.decode_image(img)
    img = tf.image.resize(img, (width, height))    
    return img

# Predicting class
def predict_img(img, model, width, height, labels):
    img = preprocess_img(img, width, height)
    pred_prob = model.predict(tf.expand_dims(img, axis=0))
    pred_cat = pred_prob.argmax(axis=-1)
    pred_class = labels[pred_cat[0]]
    
    plt.imshow(img/255.0)
    plt.title(f"Pred: {pred_class} {pred_prob.max()*100:.2f}%")
    plt.axis(False)
    plt.show()