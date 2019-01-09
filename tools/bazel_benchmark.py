import argparse
import os
import sys
import shutil
import subprocess
import tempfile

BAZEL = None
PROJECT_NAME = None
STARTUP_FLAGS = []
BUILD_FLAGS = []


def eprint(*args, **kwargs):
    """
    Print to stderr and flush (just in case).
    """
    print()
    print(*args, flush=True, file=sys.stderr, **kwargs)


def execute_command(args, shell=False, fail_if_nonzero=True):
    eprint(" ".join(args))
    return subprocess.run(args, shell=shell, check=fail_if_nonzero, env=os.environ).returncode


def bazel_build(target, extra_build_flags=[]):
    execute_command([BAZEL] + STARTUP_FLAGS + ["build"] + BUILD_FLAGS + extra_build_flags + [target])


def bazel_clean(expunge=False):
    while True:
        if execute_command([BAZEL] + STARTUP_FLAGS + ["clean"] + (["--expunge"] if expunge else []), fail_if_nonzero = False) == 0:
            break


def bazel_analyze(profile):
    execute_command([BAZEL] + STARTUP_FLAGS + ["analyze-profile", "--html", "--html_details", profile])


def bazel_version():
    execute_command([BAZEL] + STARTUP_FLAGS + ["version"])


def json_profile(target, output_base, profile_output_dir, build_type):
    profile_file = os.path.join(output_base, "command.profile")
    bazel_build(target, ["--experimental_generate_json_trace_profile"])
    shutil.move(profile_file, os.path.join(profile_output_dir, PROJECT_NAME + ("-%s.json" % build_type)))


def analyze_profile(target, output_base, profile_output_dir, build_type):
    profile_file = os.path.join(profile_output_dir, PROJECT_NAME + ("-%s.profile" % build_type))
    bazel_build(target, ["--profile=" + profile_file])
    bazel_analyze(profile_file)


def run_benchmark(target, profile_type, patch_file, profile_data_dir):

    if profile_data_dir:
        profile_output_dir = profile_data_dir
    else:
        profile_output_dir = tempfile.mkdtemp()

    output_base = subprocess.check_output([BAZEL] + STARTUP_FLAGS + ["info", "output_base"]).decode("utf-8").strip()

    profile = None
    if profile_type == "json-profile":
        profile = json_profile
        profile_output_dir = os.path.join(profile_output_dir, "json-profile")
    elif profile_type == "analyze-profile":
        profile = analyze_profile
        profile_output_dir = os.path.join(profile_output_dir, "analyze-profile")

    os.makedirs(profile_output_dir, exist_ok = True)

    bazel_clean(expunge = True)
    bazel_version() # To avoid launch time
    profile(target, output_base, profile_output_dir, "clean-expunge-build")

    bazel_clean()
    profile(target, output_base, profile_output_dir, "clean-build")

    if patch_file:
        execute_command(["patch", "-p1", "-i", patch_file])
    else:
        execute_command(["git", "checkout", "HEAD~1"])
    profile(target, output_base, profile_output_dir, "incremental-build")
    if patch_file:
        execute_command(["git", "checkout", "-f"])
    else:
        execute_command(["git", "checkout", "master"])

    eprint("Check profile results under %s" % profile_output_dir)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Script for benchmarking a bazel project")
    parser.add_argument("build_target", type=str, help="the target to build")
    parser.add_argument("--project_name", type=str, required=True, help="the name of the project to be benchmarked, this name is for renaming the profile file.")
    parser.add_argument("--bazel_binary", type=str, default="bazel", help="the bazel binary path, default is 'bazel'")
    parser.add_argument("--startup_flag", type=str, action="append", default=[], help="add a startup flag for bazel")
    parser.add_argument("--build_flag", type=str, action="append", default=[], help="add a build falg for bazel")
    parser.add_argument("--profile_type", type=str, default="json-profile", choices=["json-profile", "analyze-profile"], help="the profile type")
    # parser.add_argument("--build_type", type=str, default="all", choices=["clean-build", "clean-expunge-build", "incremental-build", "all"], help="the bazel build type")
    parser.add_argument("--patch_file", type=str, help="a patch file for the project to run the incremental build")
    parser.add_argument("--setup_command", type=str, help="a command to run before the whole benchmark builds")
    parser.add_argument("--cleanup_command", type=str, help="a command to run after the whole benchmark builds")
    parser.add_argument("--profile_data_dir", type=str, help="a directory to store all profile data")

    args = parser.parse_args(argv)

    if not args.profile_type:
        parser.print_help()

    print(args)

    global BAZEL
    global PROJECT_NAME
    global STARTUP_FLAGS
    global BUILD_FLAGS
    BAZEL = args.bazel_binary
    PROJECT_NAME = args.project_name
    STARTUP_FLAGS = args.startup_flag
    BUILD_FLAGS = args.build_flag


    if args.setup_command:
        execute_command([args.setup_command], shell = True)

    run_benchmark(args.build_target, args.profile_type, args.patch_file, args.profile_data_dir)

    if args.cleanup_command:
        execute_command([args.cleanup_command], shell = True)


if __name__ == "__main__":
    sys.exit(main())
