# vg_preprocessing
### Visual Genome dataset preprocessing

## 1. Data
Download [region_descriptions.json.zip](http://visualgenome.org/static/data/dataset/region_descriptions.json.zip)
and extract it.

## 2. Usage
Just for test, 'imgs' folder contains only first 200 images from the original dataset([images.zip](https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip))

1. '1_img_annotating.py' creates 'imgs_anno' folder to annotate the original images using the information of 'region_descriptions.json'.

2. '2_json_pruning.py' creates 'region_descriptions_pruned.json' file, which eliminates many unnecessary duplicated annotations.
