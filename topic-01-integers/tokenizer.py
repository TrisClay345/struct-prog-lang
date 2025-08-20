# Tristian Clayman

import re

patterns = [
    [r"\d*\.\d+|\d+\.\d*|\d+", "number"],
    [r"\+", "+"],
    [r".", "error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    pos = 0
    while pos < len(characters):
        # find first matching token
        for pattern, tag in patterns:
            match = pattern.match(characters, pos)
            if match:
                break

        assert match

        if tag == "error":
            raise Exception(f"Syntax error: illegal character: {[match.group(0)]}")

        token = {"tag":tag, "pos":pos}
        value = match.group(0)
        if token["tag"] == "number":
            if "." in value:
                token["value"] == float(value)
            else:
                token["value"] == int(value)
        
        tokens.append(token)
        pos = match.end()
        
    # 'end of tokens' token
    tokens.append({"tag":None, "pos":pos})
    return tokens

def test_simple_tokens():
    print("testing simple tokens...")
    assert tokenize("+") [
        {"tag":"+", "pos":0}
        {"tag":None, "pos":1}
    ]
    assert tokenize("3") [
        {"tag":"number", "pos":0, "value":3}
        {"tag":None, "pos":1}
    ]

if __name__ == "__main__":
    print("testing tokenizer...")
    test_simple_tokens()
    print("done.")

# :_(