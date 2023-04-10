# Green Lab replication package
The package has 2 directories: `android-runner-and-scenarios` and `data-and-r-script`.

## `android-runner-and-scenarios`
This directory contains a modified version of Android Runner and all scenarios used in the experiment. The scenarios can be found in `android-runner/nvw-native` and `android-runner/nvw-native`. Each of those directories has a config file per application + a directory with application-specific scripts. There is always an application-specific script called `monkeyrunner.py` containing the main code of the scenario. The last file can be executed with MonkeyRunner.

Examples:

- `android-runner/nvw-native/config-google-maps.json` contains the config file for native Google Maps.
- `android-runner/nvw-native/google_maps/monkeyrunner.py` contains the main code of the scenario.

## `data-and-r-script`
This directory contains the gathered data and the R script used for the analysis. There's 10 data directories, 2 per each application. Each of those directories contains the output of Trepn.