# Specs

* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ python3 bazel_benchmark/tools/bazel_benchmark.py //src:bazel --project_name=Bazel --profile_type=analyze-profile --profile_data_dir=bazel_benchmark/Bazel --patch_file=./test.patch
```

