import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class CosmoAiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cosmo_ai'
    # MODEL_FILE = os.path.join(settings.MODELS, "WeightPredictionLinRegModel.joblib")
    # model = joblib.load(MODEL_FILE)