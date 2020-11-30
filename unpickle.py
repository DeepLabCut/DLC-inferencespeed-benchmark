import os
import json
import numpy as np
from itertools import groupby
from pathlib import Path

def unpackdata(path):
    data = np.load(path, allow_pickle=True)
    model = data['model']
    opsys = data['op_sys']
    device = data['device'][0]
    modeltype = data['model_type']
    imsizes = data['im_size'].tolist()
    results = data['inference_times']
    results_fps = (1.0 / times for times in results)
    stats = [[np.mean(r), np.std(r)] for r in results_fps]
    return {'name': model, 'os': opsys, 'processor': device, 'model': modeltype, 'image_sizes': imsizes, 'results': stats}

files = Path("data").rglob("*.pickle")
data = [unpackdata(path) for path in files]

keyselector = lambda m:(m['name'],m['image_sizes'])
models = groupby(sorted(data, key=keyselector), key=keyselector)

Path("_data").mkdir(parents=True, exist_ok=True)
output = [
  ('_data/{0}.json'.format(name),
  {
    "name": name,
    "image_sizes": image_sizes,
    "benchmarks": [{
      "os": data['os'],
      "processor": data['processor'],
      "model": data['model'],
      "results": data['results']
    } for data in group]
  }) for (name,image_sizes), group in models]

for fname,model in output:
  print(json.dumps(model,indent=2),file=open(fname,'w'))