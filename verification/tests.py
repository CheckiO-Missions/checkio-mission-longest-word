"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["hello world"],
            "answer": "hello"
        },
        {
            "input": ["openai gpt-4"],
            "answer": "openai"
        },
        {
            "input": ["this is a sentence"],
            "answer": "sentence"
        },
        {
            "input": ["the quick brown fox"],
            "answer": "quick"
        },
        {
            "input": ["jumped over the lazy dog"],
            "answer": "jumped"
        },
        {
            "input": ["typescript is great"],
            "answer": "typescript"
        },
        {
            "input": ["the answer is 42"],
            "answer": "answer"
        },
        {
            "input": ["to be or not to be"],
            "answer": "not"
        },
        {
            "input": ["that is the question"],
            "answer": "question"
        },
        {
            "input": [""],
            "answer": ""
        },
        {
            "input": [" "],
            "answer": ""
        },
    ],
    "Extra": [
        {
            "input": ["a bc def"],
            "answer": "def"
        },
        {
            "input": ["this sentence has multiple longest words"],
            "answer": "sentence"
        },
    ]
}
