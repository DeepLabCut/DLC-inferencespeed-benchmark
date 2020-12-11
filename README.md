# DLC Inference Speed Benchmark <img src="https://images.squarespace-cdn.com/content/v1/57f6d51c9f74566f55ecf271/1606082050387-M8M1CFI5DFUZCBAAUI0W/ke17ZwdGBToddI8pDm48kLuMKy7Ws6mFofiFehYynfdZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzp2tFVMcEgqZM8QO7VXXQogrsLnYKC4n4YnYuHC1HMRWygQlqMNAoTF9HaycikLeg/DLClive.png?format=750w" width="350" title="DLC-live" alt="DLC LIVE!" align="right" vspace = "50">

This repository stores the benchmark results for [DeepLabCut-live](https://github.com/DeepLabCut/DeepLabCut-live) for each standard dataset, grouped by operating system, processor, and DLC model. Each configuration is tested on a fixed set of videos.

## How to contribute!

1. Install the [DeepLabCut-live! SDK](https://github.com/DeepLabCut/DeepLabCut-live)
2. git clone the DeepLabCut-live! repo: `git clone https://github.com/DeepLabCut/DLC-inferencespeed-benchmark.git` and run [`./reinstall.sh`](https://github.com/DeepLabCut/DeepLabCut-live/blob/master/reinstall.sh) to be sure it's properly installed.
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

This will take some time, depending on your internet connection and hardware. Note that downloading, might take a few minutes, as the multiple models & videos comprise about 2,2 GB. Then 4 models will be run on two videos for various video sizes. To get you a sense,  this takes about 90 minutes on a Titan RTX. IF you want to run the benchmark on a CPU or slow hardware, you can also change the number of frames, to 1000 in https://github.com/DeepLabCut/DeepLabCut-live/blob/master/benchmarking/run_dlclive_benchmark.py#L24.

3. Please make a pull request here (i.e., add the resulting file to your forked repo under the `_data` folder--i.e., no need to hand edit the file, we will automatically convert your files into the correct yaml file format), and create a new pull request!) or email us: admin@deeplabcut.org if you have any trouble!
