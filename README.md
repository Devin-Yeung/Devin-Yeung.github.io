## Dev

when modifying the theme (or any other submodule), use the following command to see the changes:

```bash
GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG=/dev/null HOME=/dev/null git --no-pager diff --no-color --submodule=diff > patches/patches.diff
``````
