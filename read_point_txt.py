import open3d as o3d
import numpy as np

m1 = np.loadtxt('C:\\Users\\warmtan\\Desktop\\data_processing\\10\\pcd1001.txt')[:,0:3]
source = o3d.geometry.PointCloud()
# 加载点坐标
source.points = o3d.utility.Vector3dVector(m1)
o3d.visualization.draw_geometries([source])