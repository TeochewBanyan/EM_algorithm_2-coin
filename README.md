# Algorithm Development



### Q1

My estimate to theta_a is 0.7035, the one to theta_b is 0.2767, where theta_a is the head probability of the first coin, and theta_b is the probability of the other coin.



### Q2

Before going to the core algorithm, we should obtain the data from an given url. I use requests module to get the data, using the .json method to get the content. Then via simple string method, such as striping, we could get the list of flip results.



To develop the EM algorithm for estimating coin probability, firstly I need to estimate the distribution of the hidden variable based on a prior probability of theta. In my code, I use a randomly initiated value of theta. And I use stats module to estimate hiddlen variable z, because it is easy to fit a binomial distribution using the function "pmf" from stats.



Then we could compute the expectation (contribution) that coin A and B have to the head-tail counts.  And based on the contribution, we could update the probability of each coin.



After developing the 1-iteration EM algorithm, we need to set up the iterative algorithm. I set a threshold so that the algorithm would halt when the probability converges. At the same time, a maximum iteration number is set.



Finally, to reduce errors, run the algorithm for several times (in my code, 10 times), and adopt the average as the result.

