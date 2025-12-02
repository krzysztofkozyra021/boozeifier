import tensorflow as tf
from tensorflow.keras import layers, models

BATCH_SIZE = 32
IMG_HEIGHT = 200
IMG_WIDTH = 200
DATASET_DIR = "dataset"

train_dataset = tf.keras.utils.image_dataset_from_directory(
    directory=DATASET_DIR,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    directory=DATASET_DIR,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE
)

class_names = train_dataset.class_names
print(f"Found classes: {class_names}")

AUTOTUNE = tf.data.AUTOTUNE
train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)

boozeifier_model = models.Sequential(
    [
        layers.Rescaling(1.0 / 255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        layers.Conv2D(filters=16, kernel_size=3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(units=128, activation="relu"),
        layers.Dense(len(class_names)),
    ]
)

boozeifier_model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

print("Starting training boozeifier model...")
epochs = 30
history = boozeifier_model.fit(
    train_dataset,
    epochs=epochs,
    validation_data=validation_dataset
)

model_name = "boozeifier_model.keras"

boozeifier_model.save(model_name)
print(f"Model saved as {model_name}")
