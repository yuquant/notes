# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""
import SimpleITK as sitk
import slicer
from slicer.util import *
import sitkUtils
# 导入nii图像和标签
image_path = r'D:/data/test_nii/prostate2label/images.nii.gz'
label_path = r'D:/data/test_nii/prostate2label/labels.nii.gz'
image_node = loadVolume(image_path)

label = sitk.ReadImage(label_path)
tmp_node = sitkUtils.PushVolumeToSlicer(sitkimage=label, targetNode=None,name='tmp',className='vtkMRMLLabelMapVolumeNode')
seg_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg_node.SetName('seg')
# 在现有标签的基础上叠加
# 由于缺少reference图像，似乎导入的像素会按照最小外接矩形切割，导致影响标注（区域外无法标注）
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(tmp_node, seg_node)
slicer.mrmlScene.RemoveNode(tmp_node)

# 导出和保存分割标签
# https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node
segmentation = seg_node.GetSegmentation()
seg_ids = [segmentation.GetNthSegmentID(i) for i in range(2)]
tmpNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
segmentIds = vtk.vtkStringArray()
for sid in seg_ids:
    segmentIds.InsertNextValue(sid)

segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode = seg_node, segmentIds, tmpNode, getNode('images')
# 导出到指定的labelmapVolumeNode节点，重叠的标签后边的会覆盖前边的，并且按顺序分别赋值1,2,3,4...
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
saveNode(tmpNode, 'D:/temp/labels_prostate.nii.gz')
# 在3D视图显示
seg_node.CreateClosedSurfaceRepresentation()
seg_node.SetDisplayVisibility(False)
# 删除所有的节点
slicer.mrmlScene.Clear()