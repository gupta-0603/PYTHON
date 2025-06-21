# Import necessary libraries
import keras
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import backend as K
from keras.utils import to_categorical

import numpy as np
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image

# Load and preprocess MNIST dataset
num_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# Build the CNN model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# Train the model
batch_size = 128
epochs = 10
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

# Save the trained model
model.save('mnist.h5')
print("Model saved as mnist.h5")

# Load the trained model for prediction
model = load_model('mnist.h5')

# Prediction function
def predict_digit(img):
    img = img.resize((28, 28)).convert('L')  # Resize and grayscale
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255.0
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

# Tkinter GUI App
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.title("Digit Recognizer")

        self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
        self.label = tk.Label(self, text="Draw a digit", font=("Helvetica", 24))
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)
        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_all)

        self.canvas.grid(row=0, column=0, pady=2, padx=2)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2)
        self.clear_btn.grid(row=1, column=0, pady=2)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        im = ImageGrab.grab(rect)
        digit, acc = predict_digit(im)
        self.label.configure(text=f"{digit}, {int(acc * 100)}%")

    def draw_lines(self, event):
        r = 8
        self.canvas.create_oval(event.x - r, event.y - r,
                                event.x + r, event.y + r,
                                fill='black')

# Run the app
app = App()
app.mainloop()
