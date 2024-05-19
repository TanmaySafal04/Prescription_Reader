from paddleocr import PaddleOCR, draw_ocr
# import matplotlib.pyplot as plt
import cv2
import os

# Setup model
def read_text_from_prescription(img):
    # Setup model
    ocr_model = PaddleOCR(lang='en',use_gpu=False)
    #image = cv2.imread()
    result = ocr_model.ocr(img)

    # Extracting detected components
    boxes = [result[0][res][0] for res in range(len(result[0]))]
    # Extracting text data
    texts = [result[0][res][1][0] for res in range(len(result[0]))]
    # Extracting prediciton score of detected text
    scores = [result[0][res][1][1] for res in range(len(result[0]))]

    combined_text_data=""

    for i in texts:
        combined_text_data = combined_text_data + i + " "

    return combined_text_data,boxes,texts,scores

def show_detection_with_score(img,boxes,texts,scores):


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    font_path2 = 'Roboto-Black.ttf'

    #The detection text with bounding box and prediction scores
    
    annotated2 = draw_ocr(img, boxes, texts, scores, font_path=font_path2)
    return annotated2
    plt.figure(figsize=(100,100))
    plt.imshow(annotated2)

