# Specs

* Bazel repo: 761560c2dc9af357a8457ac85e05208a4ebde48b

* Bazel version: 0.15.2

* Linux machine: SSD, 32GB RAM, 12 cores

* Windows machine: SSD, 32GB RAM, 12 cores


# Command

```sh
$ bazel clean --expunge
$ bazel run @yarn//:yarn
$ bazel build --profile=<platform>-Angular.profile //packages/core/test
$ bazel analyze-profile --html --html_details --html_histograms ./<platform>-Angular.profile
```

# Result

| Phases        | Linux         |   Windows    |
| ------------- |:-------------:| -----:|
| Total launch phase time | 28.0 ms | **205 ms** |
| Total init phase time |   1.683 s |   2.339 s |
| Total loading phase time |    197 ms |    97.1 ms |
| Total analysis phase time |   38.788 s |   **116.763 s** |
| Total preparation phase time |    6.19 ms |    **316 ms** |
| Total execution phase time |  49.289 s |  81.777 s |
| Total finish phase time | 3.72 ms | 8.46 ms |
| Total run time |  89.995 s |  201.505 s |
