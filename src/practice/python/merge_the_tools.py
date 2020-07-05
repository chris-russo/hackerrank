def merge_the_tools(s, k):
    n = len(s)
    chunks = []
    i = 0
    while i < n:
        chunk = []
        for char in s[i:i + k]:
            if chunk.count(char) == 0:
                chunk.append(char)
        chunks.append(''.join(chunk))
        i += k
    return chunks
