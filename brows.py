import requests
from bs4 import BeautifulSoup
import numpy as np
import cv2
import urllib.request
from mtcnn import MTCNN

def face_recognition(image):

    detector = MTCNN()
    # Detect faces in the image
    faces = detector.detect_faces(image)

    # Return the list of face locations
    return len(faces)

def search_img(query):
    
    headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    #  Search query on Pinterest
    url = f"https://www.freeimages.com/search/{query}"

    source = requests.get(url, headers = headers).text
    suop = BeautifulSoup(source, 'lxml')

    img_links = suop.select('img[src^="https://images.freeimages.com/images"]')


    for i in range(len(img_links)):
        img_url = (img_links[i]['src'])
        urllib.request.urlretrieve(img_url,'temp.jpg')
        # Use face_recognition to check if the image contains a face
        tempimg = cv2.imread("temp.jpg")
        face_locations = face_recognition(tempimg)

        # If the image contains a face, download it
        if face_locations > 0:
            break
        else:
            with open('temp.jpg', 'r+') as f:
                f.truncate(0)
