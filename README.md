# PRIS-CV 三维重建方向 测试

> **请将实现过程整理为 Markdown 文档，并将实现代码及所有结果一并发送至邮箱：<a href="mailto:hanyufei@bupt.edu.cn">hanyufei@bupt.edu.cn</a>。**
## 法向量渲染测试题
#### 题目要求：
在Blender中渲染一个球体的世界空间法向量图和相机空间法向量图。具体要求如下：
- 使用无光照材质直接输出法向量数据。

- 法向量需归一化并映射到RGB颜色空间（R: X轴, G: Y轴, B: Z轴）。

- 图像背景为纯黑色（RGB: [0,0,0]）。

- 最终输出为16位PNG格式图像。

#### 附加说明：
- 法向量定义：物体表面每一点的垂直方向（归一化向量）。世界空间中，法向量方向固定于全局坐标系（X/Y/Z轴）。

#### 详细教程：Blender渲染法向量图

#### 步骤1：场景初始化
1. 打开Blender（需3.0+版本，https://www.blender.org/download/）。

2. 删除默认立方体、灯光：
    - 选中灯光和立方体 → 按 Delete。
3. 添加球体：
    - 左上角选择添加（Add）->Mesh->UV sphere。
4. 调整相机参数：
    - 右上角选择相机（Cemera），之后右边的菜单选择橙色正方形的物体（Object）界面，对相机的位置和旋转方向进行调整。
    - 将transform中相机的location调整为（0，0，6），旋转角度设置为（0，0，0）。
    - 之后点击界面红绿蓝坐标系下方的相机图标进入相机视野，检查是否视野中出现了球体。
5. 调整渲染参数：
    - 右侧的菜单栏，选择相机图标的渲染（Render）属性，将场景中的渲染引擎设置为 Cycles（确保物理精度）。
    - 右侧的菜单栏，选择输出属性（Output） → 在第一栏格式（Format）中将分辨率（Resolution）设为512×512。
    最后一栏输出（Output），将文件格式（File Format）设置为OpenEXR Multilayer。
    - 右侧的菜单栏，选择观测图层属性（View Layer）→ 第二栏Passes第一栏Data中选中法向量参数Normal 。
#### 步骤2： 渲染和处理

1. 按 F12 开始渲染 → 等待进度条完成后，全屏，右上角将Combined图层调整为Normal。左上角点击图像（Image）点击保存（Save），保存至当前文件夹路径，命名为'test.exr'。
2. 打开test.py文件，确认exr_png_path与上述路径一致。
将代码补全后，运行代码，得到一张png图像。（请提前按照conda的虚拟环境，并安装OpenEXR等库）
3. 与示例的'example.png'进行比对。

### 扩展挑战
上述测试例子是世界坐标系下渲染法向量的特殊情况，即相机坐标系与世界坐标系重合。
下面我们探究如何渲染世界坐标系下的法向量并将其转换为相机坐标系。

#### 步骤3：调整相机位姿
1. 在上述操作之后，点击右上角的Camera图标，在右侧菜单栏中选择橙色正方形的物体（Object）界面，对相机的位置和旋转方向进行调整。将transform中相机的location调整为（0，6，0），旋转角度设置为（-90，0，0）。之后点击界面红绿蓝坐标系下方的相机图标进入相机视野，检查是否视野中出现了球体。
#### 步骤4： 渲染和处理
1. 按照步骤2的提升进行渲染，此时注意修改图像名为'test_world.exr'。
2. 同样运行test.py，修改exr_png_path和png_output_path后得到'test_world.png'。
3. 请与'example_world.png'进行比对，如果无误此时获得了在该视角下的世界坐标系下的法向量伪彩图。
4. 为了将其转换为相机坐标系下的法向量伪彩图，我们需要通过相机位姿来计算该视角的旋转矩阵，之后将'test_world.png'转换为'test_camera.png'。
#### 步骤5： 坐标系的转换
1. 请根据test.py中conver_world_camera该函数的提示，将代码补全，并运行代码，查看结果是否与'example_camera.png'一致。



### 参考学习网址
1. http://www.yindaheng98.top/%E5%9B%BE%E5%BD%A2%E5%AD%A6/%E7%9B%B8%E6%9C%BA%E5%8F%82%E6%95%B0%E4%B8%8E%E5%9D%90%E6%A0%87%E7%B3%BB%E5%8F%98%E6%8D%A2.html#%E6%9B%B4%E5%A4%9A%E9%98%85%E8%AF%BB%E6%9D%90%E6%96%99%EF%BC%9A
2. https://zhaoxuhui.top/blog/2018/03/13/RelationBetweenQ4&R&Euler.html
