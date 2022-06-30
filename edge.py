import cv2
import numpy as np
import math



def hough_lines_segments(edgeimage, count):

    src = cv2.imread(edgeimage, cv2.IMREAD_GRAYSCALE);

    edges = cv2.Canny(src, 150, 300)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160, minLineLength=50, maxLineGap=5)

    dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    sd = []

    if lines is not None:
        for i in range(lines.shape[0]):
            dot = []
            pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
            pt2 = (lines[i][0][2], lines[i][0][3])  # 시작점 좌표
            cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)
            # print(pt1)
            # print(pt2)

            for j in range(0, 4):
                dot.append(lines[i][0][j])
                # print(dot[j])

            x = [dot[0], dot[2]]
            y = [dot[1], dot[3]]
            slope, intercept = np.polyfit(x, y, 1)
            sd.append(slope)

        if np.std(sd) > 2:
            print("적재물이 제대로 적재 되어 있지 않습니다 ")

    cv2.imwrite("./edge/frame%d.jpg" % count, dst)

    #cv2.waitKey();
    #cv2.destroyAllWindows()