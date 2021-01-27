import numpy as np
import properscoring as ps
from scipy.stats import norm
#from cdo import Cdo
from cdo import *
cdo = Cdo()
obs = [-2, -1, 0, 1, 2]
baseline_score = ps.crps_ensemble(obs, [0, 0, 0, 0, 0]).mean()
forecast_score = ps.crps_gaussian(obs, mu=0, sig=1).mean()
skill = (baseline_score - forecast_score) / baseline_score
print(skill)
