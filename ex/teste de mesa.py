vec = ['a', 's', 'a', 'c']
cpy = vec

tmp = vec[3]
vec[0] = tmp 

tmp = cpy[2] 
cpy[2] = cpy[1]

cpy[2] = 'm'
s_vec = s_cpy = ''

for id in range (len(vec)):
  s_vec = s_vec + vec[id]
  s_cpy = s_cpy + cpy[id] 

cpy[2] = 's' 

print(s_vec)
print(s_cpy)
