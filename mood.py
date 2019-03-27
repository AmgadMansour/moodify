from image_emotion_gender_demo import  getFaceEmotion

def main_func():
    # image_path = 'C://Users/lenovo/Desktop/moodify/components/emotion-classification/images/test_image.jpg'
    #image_path = '/Users/macbookair/desktop/MS/Project/images/face1.jpg';
    image_path = 'snap.jpg'
    mood = getFaceEmotion(image_path)
    return mood
