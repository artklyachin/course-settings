import json
import os

DATA_PATH = "/data"
SETTINGS_PATH = "course-settings"

def load_course_config():
    filepath = f"{SETTINGS_PATH}/course_config.json"
    with open(filepath, "r") as f:
        return json.load(f)


def load_student_config():
    filepath = f"{DATA_PATH}/config.json"
    with open(filepath, "r") as f:
        return json.load(f)
