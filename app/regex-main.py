import re
from colorama import init, Fore

init()  # coloramaの初期化

sample_txt: str = """
This is an example sentence, but it is not the only one.
But, there was an issue.
This is another example, and it is also valid.
And that was problematic.
This is a third example, so it should be included.So the error should be corrected.
This is a fourth example, also it should be included as well.Also, there is another problem.
On one hand, the problem is now resolved.
On the other hand, a new issue arose.
In a nutshell, there are still outstanding issues to resolve.

There are lots of bugs.
There are loads of unnecessary comments.
There was plenty of time, but a lot of the billable time was wasted.

The tool is often used by sophomores.
The tool is often sometimes by alumni.

Smith finds out that the device failed.
Jones also found out the device failed.

Einstein says that quality trumps quantity.
Trump said numerous falsehoods.

It is said that to think is to be.
Right after the test, the candidates left.
Right before the test, the candidates waited outside.
Straight after the event, there was a black-out.
Straight before the event, the electricity worked as usual.
The code was amended a little bit.

When accidents happen, the respond is immediate.

Students' texts were left on the teacher's desk.

It's good that it's been discovered, but it
They're not connected to the circuit.
I'm getting tired of writing.

The expression couldn't match this example.

We've reviewed the literature.

They'd written extensively on this topic.

We'll revise the code afterwards.

It`s a Japanese apostrophe inbetween subject and verb.

This task needs to be completed ASAP.
According to Smith & Jones [1], this algorithm is the state of the art.

When should rhetorical questions be used?  Never.
"""
pattern: str = r"\b(But|And|So|Also|On one hand|On the other hand|In a nutshell)\b"

modified_sentence = re.sub(pattern, lambda match: f"{Fore.RED}{match.group()}{Fore.RESET}", sample_txt)

print(modified_sentence)