# PrivateReconstruction
A social media company wants to provide information to its advertisers on how often people
click on their ads. You work for an advertiser. Each hour, the company gives you the demographic
profile of one user who saw your ad. This demographic profile is rich enough for you to identify the
user in your own database. They also give you a running count of the number of users who have actually
clicked on your ad. They add a little bit of noise “to protect users’ privacy”, but you suspect that you
can derive a good guess as to who, exactly clicked on your ads.
We’ll model this as follows: there is a sequence x of secret bits, x1, …, xn∈ {0, 1}. The bit xi indicates
that the ith user clicked on the ad. The mechanism for releasing the running counter works as follows:
At each time step i = 1, 2, ..., n, select a uniformly random bit Zi (independently of previous ones) and
output:

![formula](https://user-images.githubusercontent.com/47434149/140687818-7232ac8e-65ed-4988-8abe-f17abc30f9a7.png)

(In other words, at each step, we flip a coin to decide whether we should add one fake person to the
counter or not).
How well can one recover the vector x from the sequence of outputs �'? The answer depends on what
we know about x ahead of time. We will consider two situations:
a) The bits of x are uniformly random and independent. The only input to the attacker is �' (the vector
of noisy counters). 
b) The bits of x are uniformly random and independent, but the attacker has some extra information.
For each i, the attacker has a guess wi which is equal to xi with probability 2/3, independently for
each i. The attacker’s inputs consist of �' and the vector of guesses �).
For each of these situations, your job is to come up with as good an algorithm as you can to guess the
entries of x. You should evaluate your algorithm by coding it up (in a language of your choice) and
plotting the fraction of bits of x recovered by your algorithm for n = 100, 500, 1000, 5000. (You should
run the algorithm on fresh random inputs at least 20 times for each value of n and report the mean and
standard deviation for each one.)
You’ll need to code up the release mechanism (i.e., the trusted party releasing information about the
dataset and not on the dataset itself), too, in order to run the experiments. You may use standard linear
algebra libraries (such as those provided by numpy in Python). You may use standard solvers for linear
systems or linear programs. 
