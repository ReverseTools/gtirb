# Unreleased

# 0.2.0

* Added a new Python API, meant to be a high-level wrapper over the
  Protobuf-generated one. To make use of it, add the `python` folder
  from your build directory to your `PYTHONPATH`. The package is named `gtirb`.
* CMake now won't automatically download and install its dependencies,
  so that the user has control over which versions are in use.
  The version requirements for Boost and Protobuf are listed in `README.md`.
* Updated the sanctioned AuxData definitions.
* Fix for build issue when using Boost 1.71.0.

# 0.1.1

* Initial public release.