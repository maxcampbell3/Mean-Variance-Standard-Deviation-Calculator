import numpy as np
import numpy as np

def calculate(list):
  if (len(list) <9):
    raise ValueError("List must contain nine numbers.")

  numMatrix= np.array(list)
  shaped = np.reshape(numMatrix,(3,3))


  out = {
      'mean': [np.mean(shaped,axis =0).tolist(),np.mean(shaped,axis =1).tolist(),np.mean(shaped)],
      'variance':[np.var(shaped,axis =0).tolist(),np.var(shaped,axis =1).tolist(),np.var(shaped)] ,
      'standard deviation':[np.std(shaped,axis =0).tolist(),np.std(shaped,axis =1).tolist(),np.std(shaped)],
      'max':[np.amax(shaped,axis =0).tolist(),np.amax(shaped,axis =1).tolist(),np.amax(shaped)] ,
      'min':[np.amin(shaped,axis =0).tolist(),np.amin(shaped,axis =1).tolist(),np.amin(shaped)] ,
      'sum': [np.sum(shaped,axis =0).tolist(),np.sum(shaped,axis =1).tolist(),np.sum(shaped)]   
  }
  
  return out