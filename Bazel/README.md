* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ bazel clean --expunge
$ bazel build --profile=<platform>-Bazel.profile //src:bazel
bazel analyze-profile --html --html_details --html_histograms ./<platform>-Bazel.profile
```

# Result

| Phases        | Linux         |   Windows    |
| ------------- |:-------------:| -----:|
| Total launch phase time | 31.0 ms | **1.527 s** |
| Total init phase time |   166 ms |   147 ms |
| Total loading phase time |    1.190 s |    **5.640 s** |
| Total analysis phase time |   5.051 s |   4.240 s |
| Total preparation phase time |    17.7 ms |    **982 ms** |
| Total execution phase time |  237.969 s |  348.364 s |
| Total finish phase time | 6.49 ms | **33.6 ms** |
| Total run time |  244.430 s |  360.933 s |
