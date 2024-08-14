import math


def calculate_angle(line1, line2):
    # 计算线段的向量表示
    vector1 = (line1[1][0] - line1[0][0], line1[1][1] - line1[0][1])
    vector2 = (line2[1][0] - line2[0][0], line2[1][1] - line2[0][1])

    # 计算点积和模
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    magnitude1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    magnitude2 = math.sqrt(vector2[0]**2 + vector2[1]**2)

    # 计算夹角的余弦值
    cosine_angle = dot_product / (magnitude1 * magnitude2)

    # 计算夹角角度
    angle_in_radians = math.acos(cosine_angle)
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees


class InferVideo:

    def __init__(self):
        pass

    def infer(self, video_path, save_path):
        pass

        # cv2.destroyAllWindows()


if __name__ == '__main__':
    infer = InferVideo()
    infer.infer("t1.mp4", "t1_out.mp4")
