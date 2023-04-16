import numpy as np

def findList(_input, error):

  num_stt = 0
  vis = []
  thho = 1500
  _out = 0
  max_location = 0
  max_value = 0

  _check = np.zeros(thho, int)
  
  file_input = _input.split('\n[')
  
  for i in range(len(file_input)):
    file_input[i] += " "
    for j in range(len(file_input[i])):
      if file_input[i][j] == "]":
        if file_input[i][j + 1] == "\n":
          _out = j
          if file_input[i][0:_out].isnumeric() == False:
            if len(vis) < 1: continue
            vis[-1] += "[" + file_input[i]
            continue
          
          local = int(file_input[i][0:_out])
          if local >= thho: continue
          _check[local] += 1
      
          vis.append("[" + file_input[i])
          if error == 1: continue
          if local > max_location:
     
            if len(vis) < 2: continue
            slpp = vis[-2].split(".........................")
            if len(slpp) < 2:
              continue
            max_location = local
            max_value = len(vis) - 2

        else: 
          if len(vis) > 0:
            vis[-1] += "[" + file_input[i]
        break
    
  _stack = 5

  for i in range(thho):
    if _check[i] > 0:
      _stack = 5
    elif _check[i] == 0:
      _stack -= 1
    if _stack <= 0:
      thho = i - 5
      break

  return vis, thho, num_stt, file_input[0], max_value

