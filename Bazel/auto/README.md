# Specs

* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ python ../../bazel_benchmark/tools/bazel_benchmark.py //src:bazel --profile_type=json-profile --project_name=Bazel --profile_data_dir=../../bazel_benchmark/Bazel/auto/Windows --patch_file=../../bazel_benchmark/Bazel/auto/bazel-inc.patch

$ python ../../bazel_benchmark/tools/bazel_benchmark.py //src:bazel --profile_type=analyze-profile --project_name=Bazel --profile_data_dir=../../bazel_benchmark/Bazel/auto/Windows --patch_file=../../bazel_benchmark/Bazel/auto/bazel-inc.patch
```

