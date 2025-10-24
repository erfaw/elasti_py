import os
import subprocess as sp; sp.call('cls', shell=True)
NUTRITIONIX_APP_ID = os.environ.get("nutritionix_app_id")
NUTRITIONIX_APP_KEY = os.environ.get("nutritionix_app_key")
print(NUTRITIONIX_APP_ID)
print(NUTRITIONIX_APP_KEY)