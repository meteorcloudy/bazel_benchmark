# Specs

* TensorFlow version: r1.10

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores

# Command

```sh
$ yes "" | ./configure
$ bazel clean
$ bazel shutdown
$ bazel build --config=opt --distinct_host_configuration=false --profile=./<platform>-TensorFlow.profile //tensorflow/tools/pip_package:build_pip_package
$ bazel analyze-profile --html --html_details --html_histograms ./<platform>-TensorFlow.profile
```

# Result

| Phases        | Linux         |   Windows    |
| ------------- |:-------------:| -----:|
| Total launch phase time | 28.0 ms | **1.513 s** |
| Total init phase time |   174 ms |   163 ms |
| Total loading phase time |    807 ms |    940 ms |
| Total analysis phase time |   3.704 s |   4.239 s |
| Total preparation phase time |    49.0 ms |    **4.364 s** |
| Total execution phase time |  1102.257 s |  1767.394 s |
| Total finish phase time | 6.31 ms | 10.2 ms |
| Total run time |  1107.026 s |  1778.624 s |