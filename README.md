

conda env create -f conda_environment_CORDEX_CORE_backup29112019.yml --> to creatze an environment


conda env update --prefix ./env --file conda_environment_CORDEX_CORE_backup29112019.yml  --prune --> when using this, I set the prefix. Better to write the prefix in the yml-file.

conda env update --file conda_environment_CORDEX_CORE_backup29112019.yml  --prune --> use this one. Then the CORDEX_CORE environment is updated

conda deactivate --> to deactivate 
