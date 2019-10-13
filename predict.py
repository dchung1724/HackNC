import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

def get_label(file_path, project_id, model_id):
  file_path = file_path
  project_id = project_id
  model_id = model_id

  with open(file_path, 'rb') as ff:
    content = ff.read()
  return get_prediction(content, project_id, model_id)
