# Specs

* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ python3 ../bazel_benchmark/tools/bazel_benchmark.py //packages/core/test/render3 --profile_type=json-profile --project_name=Angular --profile_data_dir=../bazel_benchmark/Angular/auto/Linux --patch_file=angular-inc.patch

$ python3 ../bazel_benchmark/tools/bazel_benchmark.py //packages/core/test/render3 --profile_type=analyze-profile --project_name=Angular --profile_data_dir=../bazel_benchmark/Angular/auto/Linux --patch_file=angular-inc.patch
```

