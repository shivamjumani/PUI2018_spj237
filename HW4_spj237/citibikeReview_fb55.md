# IDEA
fine

# Null hypothesis
"The proportion of customers biking on weekends is the same or lower than the proportion of subscribers biking on weekends"

you mean the "fraction"

but htis is the wrong NH: if you want to prove that subscribers ride more on weekends than costumers you have to go and prove that the opposite is false: that it is false that subscribers ride more on weekdays

# Formula

shold be the opposite: H0 : S_weekend/Stotal <=Cweekend/Ctotal

please come talk to ms if this is still not clear

# DATA
the processing is not done: you have to extract the 2 classes per user type by grouping costumers by week/weekend and subscriber by week/weekend

# TEST

this is a test for proportions: a chi sq test would be appropriate and better than a Z test, since the Z test assumes gaussianity while the chi sq test is non-parametric
https://www.r-bloggers.com/comparison-of-two-proportions-parametric-z-test-and-non-parametric-chi-squared-methods/




