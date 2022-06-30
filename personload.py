import cv2
import numpy as np
from PIL import Image
import edge
import time


def plyolo(frame, size, score_threshold, nms_threshold, count):
    # -- YOLO 포맷 및 클래스명 불러오기
    model_file = './yolov3-personload.weights'  # -- 본인 개발 환경에 맞게 변경할 것
    config_file = './yolov3-personload.cfg'  # -- 본인 개발 환경에 맞게 변경할 것
    net = cv2.dnn.readNet(model_file, config_file)
    classes2 = []
    with open("./PersonLoadNames.names", "r") as f:
        classes2 = [line.strip() for line in f.readlines()]

    # -- GPU 사용
    # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # -- 클래스의 갯수만큼 랜덤 RGB 배열을 생성
    colors = np.random.uniform(0, 255, size=(len(classes2), 3))

    # -- 이미지의 높이, 너비, 채널 받아오기
    height, width, channels = frame.shape

    # -- yolo 포맷 적용 전의 전처리
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (size, size), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # -- 전처리 결과 받아오기
    outs = net.forward(output_layers)

    # -- 탐지된 클래스 표기
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.1:
                # -- 탐지된 객체경계상자 표기
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            class_name = classes2[class_ids[i]]

            # label = f"{class_name} {confidences[i]:.2f}"
            # color = colors[class_ids[i]]
            # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            # cv2.rectangle(frame, (x - 1, y), (x + len(class_name) * 13 + 65, y - 25), color, -1)
            # cv2.putText(frame, label, (x, y - 8), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)


            if class_name=="Load":

                # 위에서 cv2.imwrite를 이용하여 만들어진 이미지를 pillow방식으로 가져옴
                reimg = Image.open("./frame/frame%d.jpg" % count)
                # 캡쳐할 부분 범위지정
                area = (x, y, x + w, y + h)
                cropped_pil = reimg.crop(area)
                # pillow방식과 cv2방식은 저장 방식이 달라서 변형
                cropped_np = np.array(cropped_pil)
                # pillow방식과 cv2방식은 rgb bgr방식으로 색상이 다름
                cropped_np = cv2.cvtColor(cropped_np, cv2.COLOR_RGB2BGR)
                #cv2.imwrite("./person-load/frame%d.jpg" % count, cropped_np)
                #cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1)

                cv2.imwrite("./person-load/frame%d.jpg" % count, cropped_np)
                edgeimage = ("./person-load/frame%d.jpg" % count)  # -- 본인 개발 환경에 맞게 변경할 것

                edge.hough_lines_segments(edgeimage, count)



            # -- 인식한 객체의 정보 출력
            #print(f"[{class_name}({i})] conf: {confidences[i]} / x: {x} / y: {y} / width: {w} / height: {h}")


