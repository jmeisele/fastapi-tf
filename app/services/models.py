"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Image classifier
"""
import numpy as np
from loguru import logger
from PIL import Image
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
    

class DoggoModel(object):

    def __init__(self):
        self._load_local_model()

    def _load_local_model(self):
        self.model = tf.keras.applications.MobileNetV2(weights="imagenet")
    
    def _pre_process(self, image):
        logger.debug('Pre-processing image')
        # Resize our image
        image = np.asarray(image.resize((224, 224)))[..., :3]
        image = np.expand_dims(image, 0)
        image = image / 127.5 - 1.0
        return image

    def _predict(self, image):
        logger.debug('Predicting...')
        prediction = self.model.predict(image)
        predictions = decode_predictions(prediction, 2)[0]
        return predictions

    def _post_process(self, predictions) -> list:
        logger.debug('Post-processing')
        response = []
        for i, res in enumerate(predictions):
            resp = {}
            resp['class'] = res[1]
            resp['confidence'] = f"{res[2]*100:0.2f} %"
            response.append(resp)
        return response

    def predict(self, payload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))
        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)
        return post_processed_result
