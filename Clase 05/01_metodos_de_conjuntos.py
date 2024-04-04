alpha = {1, 2, 3, 4}
beta = {2,3}
delta = {1, 2, 3, 4, 5}
gama = {100, 101}

# DIFERENCE
epsilon = alpha.difference(beta)
print("Alpha menos Beta", epsilon)
print()

# UNION
omega = alpha.union(gama)
print("Union de alpha y gama", omega)
print()

# ISSUPERSET
print("Alpha contiene a Beta: ", alpha.issuperset(beta))
print("Gama contiene a Beta: ", gama.issuperset(beta))
print()

# ISSUBSET
print("Beta es subconjunto con Alpha: ", beta.issubset(alpha))
print("Beta es subconjunto con Gama: ", beta.issubset(gama))
print()

# ISDISJOINT
print("Alpha es disjunto con Beta: ", alpha.isdisjoint(beta))
print("Alpha es disjunto con Gama: ", alpha.isdisjoint(gama))
print()

# COPY
mi_conjunto = beta.copy()
print(mi_conjunto)
mi_conjunto.add("7")
print(mi_conjunto)