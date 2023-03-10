from mmseg.apis import inference_segmentor, init_segmentor
import mmcv

config_file = 'F:/mmsegemantation/mmsegmentation/configs/vit/upernet_vit-b16_mln_512x512_80k_ade20k.py'
checkpoint_file = 'F:/Python_test/upernet_vit-b16_mln_512x512_80k_ade20k_20210624_130547-0403cee1.pth'

# build the model from a config file and a checkpoint file
model = init_segmentor(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = './test3.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_segmentor(model, img)
# visualize the results in a new window
model.show_result(img, result, show=True)
# or save the visualization results to image files
# you can change the opacity of the painted segmentation map in (0, 1].
model.show_result(img, result, out_file='result.jpg', opacity=0.5)