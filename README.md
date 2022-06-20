# CCorp Ruamel.YAML Include Extension

This package is exactly ccorp-yaml-include package(a fork of ccorp-yaml-include) that contains a bug fix (init of YAML didn't accept a 'typ' kwargs that was a list)
It also allows to use `!include` tag with a relative path for aliases, e.g.
instead of just writing: 
<br> *!include bear_common.yaml* <br>(which means that bear_common.yaml should be located in the same directory as your yaml file) 

you can have:
<br>*!include ../common_data/bear_common.yaml* <br>(which means that bear_common.yaml in now located in a separate folder 'common_data')
- **version 0.0.4**: a bug related to ExcludingConstructor.construct_sequence() method to miss a parameter called 'deep', fixed.

**IT'S fork of https://github.com/marsoloGit/ccorp_yaml_include.**

**First original repo is https://github.com/Tristan-Sweeney-CambridgeConsultants/ccorp_yaml_include**
