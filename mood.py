from image_emotion_gender_demo import  getFaceEmotion

def main_func():
    image_path = 'C://Users/lenovo/Desktop/moodify/components/emotion-classification/images/test_image.jpg'
    mood = getFaceEmotion(image_path)
    return mood
