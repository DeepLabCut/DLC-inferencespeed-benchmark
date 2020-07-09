---
layout: default
title: Benchmarks
---

{% for dataset in site.data %}
<table>
  <thead>
    <tr>
        <th colspan="3">{{dataset[1].name}}</th>
        <th colspan="{{dataset[1].image_sizes.size}}">Image Size</th>
    </tr>
    <tr>
        <th></th>
        <th>Processor</th>
        <th>DLC Model</th>
        {% for size in dataset[1].image_sizes %}
        <th>{{size}}</th>
        {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% assign os_benchmarks = dataset[1].benchmarks | group_by:"os" %}
    {% for os in os_benchmarks %}
    {% assign os_line = true %}
    {% assign processor_benchmarks = os.items | group_by:"processor" %}
    {% for processor in processor_benchmarks %}
    {% for benchmark in processor.items %}
    <tr>
        {% if os_line == true %}
        <td rowspan="{{os.items.size}}">{{os.name}}</td>
        {% assign os_line = false %}
        {% endif %}
        {% if forloop.first == true %}
        <td rowspan="{{processor.items.size}}">{{processor.name}}</td>
        {% endif %}
        <td>{{benchmark.model}}</td>
        {% for result in benchmark.results %}
        <td>{{result[0]}}±{{result[1]}}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    {% endfor %}
    {% endfor %}
  </tbody>
</table>
{% endfor %}