# Linux

```sh
$ yes "" | ./configure
$ bazel clean --expunge
$ bazel shutdown
$ bazel build --config=opt --distinct_host_configuration=false --profile=./Linux-TensorFlow.profile //tensorflow/tools/pip_package:build_pip_package
$ bazel analyze-profile --html --html_details --html_histograms ./Linux-TensorFlow.profile
```

# Windows

```sh
$ yes "" | ./configure
$ bazel clean --expunge
$ bazel shutdown
$ bazel build --config=opt --distinct_host_configuration=false --profile=./Windows-TensorFlow-<>.profile //tensorflow/tools/pip_package:build_pip_package
$ bazel analyze-profile --html --html_details --html_histograms ./Windows-TensorFlow-<>.profile
```

# Result

| Phases        | Linux         |   Windows    |
| ------------- |:-------------:| -----:|
| Total launch phase time | 28.0 ms | **1.509 s** |
| Total init phase time |  187 ms  | 150 ms |
| Total loading phase time |   1.296 s | **7.241 s** |
| Total analysis phase time |  6.390 s | **180.133 s** |
| Total preparation phase time |   47.7 ms | **2.423 s** |
| Total execution phase time | 1106.803 s  | 1825.458 s |
| Total finish phase time |9.47 ms | 9.98 ms |
| Total run time | 1114.762 s  | 2016.925 s |
