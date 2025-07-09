import OpenEXR
import numpy as np
import cv2
import Imath
exr_png_path = "test.exr"
png_output_path = "test.png"
def get_exr_cmpnt(exr_file, key, size_hw):
    pt = Imath.PixelType(Imath.PixelType.FLOAT)
    return np.frombuffer(exr_file.channel(key, pt), dtype=np.float32).reshape(size_hw)

def convert_exr_to_png(exr_path, png_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(exr_path)
    
    # Get the header and channels
    dw = exr_file.header()['dataWindow']
    width = dw.max.x - dw.min.x + 1
    height = dw.max.y - dw.min.y + 1
    hw = (height, width)
    normal_channel_names = ['ViewLayer.Normal.X', 'ViewLayer.Normal.Y', 'ViewLayer.Normal.Z']
    normals = np.stack([get_exr_cmpnt(exr_file, name, hw) for name in normal_channel_names], -1)

    '''
    此处需要补全代码，请从法向量的定义出发，考虑其取值范围等
    将法向量映射为[0,1]范围内的RGB值（R、G、B对应法向量的X、Y、Z分量）
    使用OpenCV将其保存为PNG格式的16bit图像（注意通道顺序问题）
    '''

def convert_world_camera(world_png_path, camera_png_path,
                         rotation):   

    world_normal = cv2.imread(world_png_path, cv2.IMREAD_UNCHANGED)
    '''
    此处需要补全代码，读取世界空间法向量图像并进行预处理
    '''


    rx, ry, rz = np.radians(rotation)
    '''
    此处需要补全代码，计算绕X轴,y轴和z轴的旋转矩阵
    '''

    # 计算 matrix (R = Rz * Ry * Rx)
    # camera_normal = np.einsum('ij,...j', np.linalg.inv(R), world_normal)
    '''
    此处需要补全代码，保存图像为16bit PNG格式
    '''

# Convert EXR to PNG

# 第一题
exr_png_path = "test.exr"
png_output_path = "test.png"
convert_exr_to_png(exr_png_path, png_output_path)

# 扩展挑战
# exr_png_path = "test_world.exr"
# png_output_path = "test_world.png"
# convert_exr_to_png(exr_png_path, png_output_path)

# rotation = [-90, 0, 0]  
# convert_world_camera(png_output_path, "test_camera.png", rotation)