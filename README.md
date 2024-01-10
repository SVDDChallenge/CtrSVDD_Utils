# Utility Scripts for SVDD Challenge 2024

This repository contains code related to the SVDD Challenge 2024 CtrSVDD dataset. The training and development sets are available for download at [zenodo](https://zenodo.org/doi/10.5281/zenodo.10467604).

## Understanding Dataset

Each line within `train.txt` and `dev.txt` denotes one song clip's metadata. The lines looks like this:
```
m4singer CtrSVDD_0110 CtrSVDD_0110_D_0015416 - - bonafide
jvsmusic CtrSVDD_0097 CtrSVDD_0097_D_0010993 - A06 deepfake
```
From left to right, the fields denote original dataset containing singer identity, CtrSVDD singer ID, file name (corresponding `*.flac` file is in `train_set.zip` and `dev_set.zip` correspondingly), attack (labeled as Axx), and bonafide or deepfake.

This metadata list is designed to be of similar format as ASVspoof2019LA. With small modifications, you should be able to get existing ASVspoof2019LA dataloaders up and running quickly.

## Generating the full dataset
SVDD Challenge 2024 Training and Development Dataset is provided under BY-NC-ND 4.0 license ([Read legal code](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.en)) while some of our bonafide utterances are issued under more restrictive licenses. In accordance to this issue, although our provided metadata (`train.txt` and `dev.txt`) contains all entries, our provided audio files (`train_set.zip` and `dev_set.zip`) do not. 

Therefore, participants need to download [Oniku](http://onikuru.info/db-download/), [Ofuton](https://sites.google.com/view/oftn-utagoedb/%E3%83%9B%E3%83%BC%E3%83%A0), [Kiritan](https://zunko.jp/kiridev/login.php) and [JVS-MuSiC](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_music) themselves. 

After downloading, this repository provides several timestamp files (`timestamps/{dataset}_timestamps_{split}.txt`) to help you with segmenting and renaming.

Run each timestamp file against the corresponding dataset path with our provided segmentation script:

`python segment.py {dataset_directory} {timestamp_file} {output_directory}`

`dataset_directory` should be the base directory of each dataset (`jvs_music_ver1`, `kiritan_singing/wav`, `OFUTON_P_UTAGOE_DB`, `ONIKU_KURUMI_UTAGOE_DB`);

`output_directory` should be the extracted `train/` or `dev/` directory containing the provided SVDD Challenge training or development set audio.

## Metrics
We provide a short example script, implemented using `numpy` in `eer.py` for calculating the detection error tradeoff (DET) curve and equal error rate (EER), which we use as the main metrics of the challenge.

For any SVDD system, we expect the output to be a number. Similar to all binary classification problems, we can select a threshold, where we denote any number larger than this threshold is deepfake, and any number smaller than this threshold is bonafide.

DET curve plots the false negative rate against false positive rate, where we can see how as threshold changes, both values changes. The optimal point on this curve is where false negative rate equals false positive rate. We denote the rate at this point as "equal error rate," or EER. EER is characteristic of a SVDD system's overall performance.