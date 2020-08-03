# DLC-inferencespeed-benchmark

This repository stores the benchmark results for [DeepLabCut-live](https://github.com/DeepLabCut/DeepLabCut-live) for each standard dataset, grouped by operating system, processor, and DLC model. Each configuration is tested on a fixed set of image sizes.

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

## How to contribute

1. Install the [DeepLabCut-live](https://github.com/DeepLabCut/DeepLabCut-live) SDK
2. Follow the [benchmarking instructions](https://github.com/DeepLabCut/DeepLabCut-live#benchmarkinganalyzing-exported-deeplabcut-models) for exported DLC models
3. Calculate the `mean` and `std` in frames per second for each of your benchmarks
4. Fork the repository
5. If testing a new configuration on the standard datasets, find the matching dataset in the `_data` folder (e.g. `dog.yml` or `mouse.yml`); otherwise, create a new YML file for your dataset
6. Add an entry for your new benchmark:
```yml
  - os: Linux
    processor: Intel Xeon CPU 3.1 GHz
    model: ResNet-50
    results: [[24,1], [11,0], [3,0], [2,0], [1,0]]
```
7. Submit a pull-request