# DLC Inference Speed Benchmark <img src="https://images.squarespace-cdn.com/content/v1/57f6d51c9f74566f55ecf271/1606082050387-M8M1CFI5DFUZCBAAUI0W/ke17ZwdGBToddI8pDm48kLuMKy7Ws6mFofiFehYynfdZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzp2tFVMcEgqZM8QO7VXXQogrsLnYKC4n4YnYuHC1HMRWygQlqMNAoTF9HaycikLeg/DLClive.png?format=750w" width="350" title="DLC-live" alt="DLC LIVE!" align="right" vspace = "50">

This repository stores the benchmark results for [DeepLabCut-live](https://github.com/DeepLabCut/DeepLabCut-live) for each standard dataset, grouped by operating system, processor, and DLC model. Each configuration is tested on a fixed set of videos.

## How to contribute!

1. Install the [DeepLabCut-live!](https://github.com/DeepLabCut/DeepLabCut-live) SDK
2. git clone the repo: `git clone git@github.com:DeepLabCut/DLC-inferencespeed-benchmark.git` and run `./reinstall.sh` to be sure it's properly installed.
2. Run our benchmarking script on your system (with our data/model). Within the DeepLabCut-Live directory you will find the following structure:
```
DeepLabCut-Live
   -Benchmarking
   --> run_dlclive_benchmark.py
```
Then you can run (with python3, pythonw on MacOS):
```python
python run_dlclive_benchmark.py
```
This will take some time, depending on your internet connection-- the videos are large to get stable values during benchmarking.

3. Please make a pull request (i.e., add the resulting file to your forked repo under the `_data` folder, and create a new pull request!) or email us: admin@deeplabcut.org if you have any trouble!

## Benchmark YAML file

The table is automatically generated from YAML files in the `_data` folder using the GitHub Pages [Jekyll](https://jekyllrb.com/docs/liquid/) engine. Below is a snippet from the file:

```yml
name: Dog Video
image_sizes: ["75 x 33", "150 x 267", "300 x 533", "424 x 754", "600 x 1067"]
benchmarks:
  - os: Linux
    processor: Intel Xeon CPU 3.1 GHz
    model: MobileNetV2-0.35
    results: [[62,5], [31,1], [14,0], [8,0], [4,0]]
    
  - os: Linux
    processor: Intel Xeon CPU 3.1 GHz
    model: ResNet-50
    results: [[24,1], [11,0], [3,0], [2,0], [1,0]]
```

The header section specifies the `name` of the table, and the list of `image_sizes` which were tested for each particular dataset.

The block collection `benchmarks` contains the structured list of individual table entries. For each row you will need to specify the `os`, `processor`, `model`. These will be used to group the entries in the table, so make sure to keep to the standardized names.

The `results` entry for each benchmark is a list of `[mean,std]`, in frames per second, containing the results of running the benchmark for each of the image sizes declared at the top of the file. For the table to format correctly, all lists need to have the same number of results.

YAML files can be quite picky with indenting, so when editing the file manually be careful with lining up the dashes. If any error messages show up, beware that the line indicated in the error message might not correspond to the actual where the problem is.
