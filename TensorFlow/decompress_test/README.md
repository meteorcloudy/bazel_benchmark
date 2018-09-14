Download and decompress TensorFlow dependencies

# With Windows Defender:

download:
real    0m3.629s
user    0m1.485s
sys     0m1.135s

decompress:
real    2m3.613s
user    0m2.854s
sys     0m36.190s

# Without Windows Defender (C:/src):

download:
real    0m3.564s
user    0m1.437s
sys     0m1.155s

decompress:
real    0m50.691s
user    0m2.764s
sys     0m36.574s

# Linux:

download:
real    0m1.897s
user    0m0.832s
sys     0m0.476s

decompress:
real    0m2.217s
user    0m1.840s
sys     0m1.060s


-----------------------------------------------------------------------------------------------------------

bazel version 0.15.2
Run `bazel build --config=opt --distinct_host_configuration=false --profile=./<platform>-TensorFlow.profile //tensorflow/tools/pip_package:build_pip_package --nobuild`

# With Windows Defender:

INFO: Analysed target //tensorflow/tools/pip_package:build_pip_package (262 packages loaded).
INFO: Found 1 target...
INFO: Elapsed time: 138.772s
INFO: 0 processes.
INFO: Build completed successfully, 0 total actions

# Without Windows Defender (C:/src):

INFO: Analysed target //tensorflow/tools/pip_package:build_pip_package (262 packages loaded).
INFO: Found 1 target...
INFO: Elapsed time: 65.741s
INFO: 0 processes.
INFO: Build completed successfully, 0 total actions

# Linux:

INFO: Analysed target //tensorflow/tools/pip_package:build_pip_package (309 packages loaded).
INFO: Found 1 target...
INFO: Elapsed time: 6.973s
INFO: 0 processes.
INFO: Build completed successfully, 0 total actions