import functools
import unicodedata

nfc = functools.partial(unicodedata.normalize, "NFC")
s1 = "café"
s2 = "cafe\u0301"

print("s1, s2", s1, s2)  # ('café', 'café')
print("s1 == s2", s1 == s2)  # False
print("nfc(s1) == nfc(s2)", nfc(s1) == nfc(s2))  # True
