The reflection design pattern is something I've used in many applications, and it's surprisingly easy to implement.Just as humans will sometimes reflect their own output and find a way to improve it.

Let's take a look for this exemple:

I trying to write some source Code:

```
def my_function(args):
  ....
```

And for any reason, the code dont meet the perfection that we want so, you need to rewrite code until we get the needed target.

reflect much more deeply and figure out what may be going wrong, if anything, and results in a much better second version of the code than if there wasn't this external information that you can ingest.So one thing to keep in mind, whenever reflection has an opportunity to get additional information, that makes it much more powerful.

So what is the beneficts to use a reflection instead of on shot prompting ?

* specify criteria to check
* clearly indicate the the reflection action
* checking improving performance on our specific application.
* using more than LLM to review the first draft output ...

**Evaluate the impact of reflection**

1. Objective evaluation

Based on hard facts, data, and observable metrics that do not change based on who is looking.

* Code based eval are easier
* buil a dataset of ground truth  examples

2. Subjective evaluation

Based on personal opinions, viewpoints, interpretations, and qualitative observations.

* Use LLM as a judge
* Rubric-based grading is better

**Using external feedback**

Reflection with external feedback, if you can get it, is much more powerful than reflection, so the only source of new information isn't just an LM reflecting, it'S an external informations or simply tool that we developpe to get a accurate prompte wich feet with our context boundries.
