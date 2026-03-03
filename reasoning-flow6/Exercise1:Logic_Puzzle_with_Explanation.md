# Objective: Guide the model to solve a problem with explicit reasoning.

# Question1 = Write a logic puzzle (e.g., "Alice is older than Bob, Bob is older than Carol. Who is the youngest?").


    They have four neighbours, John, Joy,Favour and Solomon. They each likes different food: yam, beans, rice, and spaghetti.
    Clues:
    1. Joy does not like yam
    2. Favour likes spaghetti
    3. John likes rice

# Question2 = Prompt the model: "Explain your reasoning before giving the final answer."

After asking AI:
Given:

People:

John

Joy

Favour

Solomon

Foods (all different):

Yam

Beans

Rice

Spaghetti

🔎 Step 1: Use the direct clues first
Clue 2:

Favour likes spaghetti

So:

Favour = Spaghetti

No one else can like spaghetti.

Clue 3:

John likes rice

So:

John = Rice

Now rice is taken.

🔎 Step 2: Update remaining options

So far we have:

Favour → Spaghetti

John → Rice

Remaining foods:

Yam

Beans

Remaining people:

Joy

Solomon

Clue 1:

Joy does not like yam

Since only Yam and Beans are left, and Joy cannot have Yam:

Joy = Beans

That leaves:

Solomon = Yam

Final Answer

John → Rice

Favour → Spaghetti

Joy → Beans

Solomon → Yam

# Question3 = Verify that the model provides step-by-step reasoning followed by the correct answer.
 
    The model did give a step by step answer and reasoning