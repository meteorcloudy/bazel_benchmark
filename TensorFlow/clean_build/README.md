# Linux

```sh
$ yes "" | ./configure
$ bazel clean
$ bazel shutdown
$ bazel build --config=opt --distinct_host_configuration=false --profile=./Linux-TensorFlow.profile //tensorflow/tools/pip_package:build_pip_package
$ bazel analyze-profile --html --html_details --html_histograms ./Linux-TensorFlow.profile
```

# Windows

```sh
$ yes "" | ./configure
$ bazel clean
$ bazel shutdown
$ bazel build --config=opt --distinct_host_configuration=false --profile=./Windows-TensorFlow.profile //tensorflow/tools/pip_package:build_pip_package
$ bazel analyze-profile --html --html_details --html_histograms ./Windows-TensorFlow.profile
```
