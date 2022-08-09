# levy-flight
Computational model of a bounded Lévy Flight 

Lévy flight represents a model of understanding we have for reaching a target destination. 
Recent [studies](https://pubmed.ncbi.nlm.nih.gov/33419738/) aim to model the single cell walk of E.Coli in search of 
nutrients using this methodology. We think this can be roughly applied to models of Immune cell migration and can 
increase the physiological accuracy of certain computational models. 

The [Lévy distribution](https://en.wikipedia.org/wiki/L%C3%A9vy_distribution) is a non-negative heavy-tail distribution. Sampling along this distribution will ensure many variates of small value and few of large value. 
The distance traveled at each timestep is sampled along this distribution but is truncated 
at the `max_dist` value. Movement in either the positive or negative distribution is determined
using a simple pseudorandom `bool(0 or 1)` in Python. 

We calculate distance at the `k+1` timestep as follows: 
`x_k+1 = x_k + v_k` where `v` is Lévy random distributed

