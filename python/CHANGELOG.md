Changelog for `gpustat`
=======================

## Unreleased

* Alias `gpustat --watch` to `-i`/`--interval` option.


## [v0.5.0][milestone-0.5]

* [Feature] Built-in watch mode (`gpustat -i`) (#7, #41).
   * Contributed by @drons and @Stonesjtu, Thanks!
* [Bug] Fix the problem extra character was showing (#32)
* [Bug] Fix a bug in json mode where process information is unavailable (#45)
* [Etc.] Refactoring of internal code structure: `gpustat` is now a package (#33)
* [Etc.] More unit tests and better use of code styles (flake8)

[milestone-0.5]: https://github.com/wookayin/gpustat/issues?utf8=%E2%9C%93&q=milestone%3A0.5


## v0.4.1
* Fix a bug that might happen when power_draw is not available (#16)


## v0.4.0

`gpustat` is no more a zero-dependency script and now depends on some packages. Please install using pip.

- Use `nvidia-ml-py` bindings and `psutil` to replace command-line call of `nvidia-smi` and `ps` (#20, Thanks to @Stonesjtu).
- A behavior on pipe is changed; it will not be in color by default, use `--color` explicitly. (e.g. `watch --color -n1.0 gpustat --color`)
- Fix a bug in handling stale-state or zombie process (#16)
- Include non-CUDA graphics applications in the process list (#18, Thanks to @kapsh)
- Support power usage (#13, #28, Thanks to @cjw85)
- Support `--debug` option


## v0.3.1

- Experimental JSON output feature (#10)
- Add some properties and dict-style access for `GPUStat` class
- Fix Python3 compatibility


## v0.2.0

- Add `--gpuname-width` option
- Display long usernames correctly
- Support older NVIDIA cards (#6)
