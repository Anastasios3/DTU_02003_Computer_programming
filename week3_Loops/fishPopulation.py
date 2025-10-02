"Fish population is modeled bu N(new) = N(old) + 0,25*N(old) - 1000. "
"How will it evolve in 5 years?"

# That's how I did it:

# N=10000
# year=0
# while year<5:
#     N=N+0.25*N-1000
#     year=year+1
# print("The fish population after 5 years will be:", N)

r = 0.25
population = 1500
licenses = 1000
nr_years = 7

for i in range(nr_years):
    population = population + r * population - licenses
    print("The fish population after", i + 1, "years will be:", population)
    