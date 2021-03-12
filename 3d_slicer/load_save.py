# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""
import SimpleITK as sitk
import slicer
import sitkUtils
image_path = r'D:/data/test_nii/prostate2label/images.nii.gz'
label_path = r'D:/data/test_nii/prostate2label/labels.nii.gz'
image_node = loadVolume(image_path)
label = sitk.ReadImage(label_path)
tmp_node = sitkUtils.PushVolumeToSlicer(sitkimage=label, targetNode=None,name='tmp',className='vtkMRMLLabelMapVolumeNode')
seg_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg_node.SetName('seg')
# 在现有标签的基础上叠加
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(tmp_node, seg_node)
slicer.mrmlScene.RemoveNode(tmp_node)
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