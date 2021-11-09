from parameters import GroupParameters, KnownParameters

group = KnownParameters.ExampleDsa_160

p = group.prime
g = group.generator
q = group.subgroupSize

print(p, len(str(p)), "\n")
print(g, len(str(g)), "\n")
print(q, len(str(q)), "\n")
