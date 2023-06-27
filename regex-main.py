import re
from colorama import init, Fore

init()  # coloramaの初期化

sample_txt: str = """
But, there was an issue.
And that was problematic.
So the error should be corrected.
Also, there is another problem.

On one hand, the problem is now resolved.
On the other hand, a new issue arose.
In a nutshell, there are still outstanding issues to resolve.

There are lots of bugs.
There are loads of unnecessary comments.
There was plenty of time, but a lot of the billable time was wasted.
She has a lot of books in her personal library.

The tool is often used by sophomores.
The tool is sometimes used by alumni.

Smith finds out that the device failed.
Jones also found out the device failed.

Einstein says that quality trumps quantity.
He didn't say anything during the meeting.
Trump said numerous falsehoods.
It is said that to think is to be.

Right after the test, the candidates left.
Right before the test, the candidates waited outside.
Straight after the event, there was a blackout.
Straight before the event, the electricity worked as usual.
The code was amended a little bit.

When accidents happen, the response is immediate.
It happens every day at the same time.
I missed the meeting because it happened while I was away.

Students' texts were left on the teacher's desk.

It's good that it has been discovered, but it

They're not connected to the circuit.

I'm getting tired of writing.

The expression couldn't match this example.

We've reviewed the literature.
They'd written extensively on this topic.

We'll revise the code afterwards.

It`s a Japanese apostrophe between the subject and verb.

This task needs to be completed as soon as possible.

According to Smith & Jones [1], this algorithm is the state of the art.

When should rhetorical questions be used? Never.
"""

patterns = [
    (r"\b(But|And|So|Also)\b", Fore.BLUE),
    (r"\b(On one hand|On the other hand|In a nutshell)\b", Fore.BLUE),
    (r"\b(lots of|loads of|plenty of|a lot of)\b", Fore.YELLOW),
    (r"\b(often|sometimes)\b", Fore.YELLOW),
    (r"\b(find out|finds out|found out)\b", Fore.YELLOW),
    (r"\b(say|says|said|It is said)\b", Fore.YELLOW),
    (r"\b(Right after|Right before|Straight after|Straight before|little bit)\b", Fore.YELLOW),
    (r"\b(happen|happens|happened)\b", Fore.YELLOW),
    (r"\b's\b", Fore.MAGENTA),
    (r"\b(It's|it's|'re|I'm)\b", Fore.MAGENTA),
    (r"\b\w+n't\b", Fore.MAGENTA),
    (r"\b('ve|'d)\b", Fore.MAGENTA),
    (r"\b'll\b", Fore.MAGENTA),
    (r"\b`\b", Fore.MAGENTA),
    (r"\bas soon as possible\b", Fore.MAGENTA),
    (r"\&", Fore.MAGENTA),
    (r"\?", Fore.MAGENTA)
]

def highlight_text(text):
    for pattern, color in patterns:
        text = re.sub(pattern, f"{color}\\g<0>{Fore.GREEN} This expression is not formal{Fore.RESET}", text)
    return text

highlighted_text = highlight_text(sample_txt)
print(highlighted_text)
