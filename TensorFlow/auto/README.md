# Specs

* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ python3 ../bazel_benchmark/tools/bazel_benchmark.py //tensorflow/tools/pip_package:build_pip_package --build_flag="--config=opt" --profile_type=json-profile --project_name=TensorFlow --profile_data_dir=../bazel_benchmark/TensorFlow/auto/Linux --setup_command='yes "" | ./configure' --build_flag="--distinct_host_configuration=false"

$ python3 ../bazel_benchmark/tools/bazel_benchmark.py //tensorflow/tools/pip_package:build_pip_package --build_flag="--config=opt" --profile_type=analyze-profile --project_name=TensorFlow --profile_data_dir=../bazel_benchmark/TensorFlow/auto/Linux --setup_command='yes "" | ./configure' --build_flag="--distinct_host_configuration=false"
```

