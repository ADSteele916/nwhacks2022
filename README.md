# Au Delà

## Summary

### Teacher

The main functionality of our project is the semantic autograder. Classically, autograders rely on black-box testing. This approach obviously works well for tasks like grading problem sets and exams but falls short in some other settings. Studies show that active participation in lectures boosts learning outcomes. To encourage this, profs might have students submit code for autograding live in lectures to incentivize participation. However, this can backfire, as the autograder forces students to write perfect code while also being introduced to a topic for the first time, which distracts them from actually learning.

Ideally, an autograder would be able to tell that a student is writing code that, while not necessarily correct, shows that they understand the problem and roughly know what a solution might look like. To fill this void, we designed a semantics-based autograder. It uses GPT-3 to look at the contents of a student's code submission and determine how closely it resembles a solution for the given problem. The benefits of using a natural language model, rather than classical text parsing and diffing, to solve this problem are manifest. First, the semantic autograder is able to extract meaning, rather than just structure, from code. This prevents false negatives from similar-looking functions (like `submission_wrong_function.py`), which can easily arise when a course enforces a common template for certain functions. It also prevents false positives when a problem allows for extremely diverse solutions (such as `submission_iterative.py`) that can vary wildly from what the instructor expects while still solving the problem.

### Student



## Technology

Our implementation uses OpenAI's Python API and a Flask backend.

## Running

Unfortunately, OpenAI doesn't allow projects using GPT-3 to be published without approval, which takes around two weeks. We are, however, allowed to share pre-generated results, as we did in our demonstration video. Additionally, if you have an API key, you are free to run our code and verify our results. Simply clone the repository, add your key as an environment variable named `OPENAI_API_KEY`, and run `comparisons/comparison_funcs.py`. Here are the expected results:
```
fibonacci/starter.py: (105.779, 48.065, -57.714); Passing = False
fibonacci/submission_random_garbage.py: (4.357, 3.657, -0.7000000000000002); Passing = False
fibonacci/submission_wrong_function.py: (25.971, 18.292, -7.6789999999999985); Passing = False
fibonacci/submission_recur.py: (25.715, 33.526, 7.8110000000000035); Passing = True
fibonacci/submission_invalid.py: (18.612, 37.666, 19.054); Passing = True
fibonacci/submission_indent_error.py: (11.573, 60.106, 48.533); Passing = True
fibonacci/solution.py: (10.018, 57.529, 47.511); Passing = True
bintree/starter.py: (14.276, 7.852, -6.4239999999999995); Passing = False
bintree/submission_iterative.py: (1.316, 3.952, 2.636); Passing = True
bintree/submission_alternative.py: (3.74, 5.479, 1.7389999999999999); Passing = True
bintree/solution.py: (1.539, 7.248, 5.7090000000000005); Passing = True
```
As we can see, handing in either starter file fails, as does typing random Python code or solving the wrong problem. However, all of the partial attempts at a solution get credit, which is what we want.
