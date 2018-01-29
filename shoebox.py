from watson_developer_cloud import VisualRecognitionV3
import json
from os.path import join, dirname
from os import environ


def classify_image_url(image_url):
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='a62b8c9c316c64b54cfd6e0da6ea7617fdf4d2b5')
    data = visual_recognition.classify(images_url=image_url)

    object_list = []
    for num in range(5):
        object_list.append(data['images'][0]['classifiers'][0]['classes'][num]['class'])
    return object_list


def classify_local_image(image_path):
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='a62b8c9c316c64b54cfd6e0da6ea7617fdf4d2b5')
    with open(join(dirname(__file__), image_path), 'rb') as image_path:
        data = visual_recognition.classify(images_file=image_path)

    object_list = []
    for num in range(5):
        object_list.append(data['images'][0]['classifiers'][0]['classes'][num]['class'])
    return object_list



def database_function():
    database = ["shoebox", "glass", "soda", "cardboard", "plastic", "can", "beer", "box", "water", "bottled"]
    return database


def relevant_object_url(image_url):
    database = database_function()
    object_list = classify_image_url(image_url)
    for element in object_list:
        if element in database:
            return #html_file
        else:
            return #default_html_file

def relevant_object_local(image_path):
    database = database_function()
    object_list = classify_local_image(image_path)
    for element in object_list:
        if element in database:
            return  # html_file
        else:
            return  # default_html_file

