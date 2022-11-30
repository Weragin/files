# import numpy
#
#
# with open("data_1/data.txt", "r", encoding="utf-8") as mask:
#     with open("data_1/lorem_ipsum.txt", "r") as lipsum:
#         with open("data_1/convolution-data-and-lorem_ipsum.txt", "w") as convolution:
#             msk = mask.read()
#             lps = lipsum.read()
#             convolution.write(str(numpy.convolve(msk, lps)))
#

fr = open("data_1/data.txt", "r")
abc = {}
for line in fr:
    for char in line:
        if char.isupper() or char.islower():
            abc[char.lower()] = abc.get(char.lower(), 0) + 1

print(abc)

# oblubena knizka - kucera, maturujeme v pythone:
# konzolove ulohy, 2 a 4
