text = "X-DSPAM-Confidence:    0.8475";

colonpos = text.find(":")
print(colonpos)

numpos = text.find("0.8475")
print(numpos)

num = text[colonpos+1:]
out = float(num)
print(out)
