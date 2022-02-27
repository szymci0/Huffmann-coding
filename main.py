# Huffman Coding in python


# Creating tree nodes
class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


def message_input():
    # Asks user for a input
    message = input("Please write your message: ")
    return message.strip()


def message_extract(message):
    # Extracts message and deletes spaces between words
    arr = list(message.lower())
    print(arr)
    delete_empty = [ele for ele in arr if ele.strip()]
    return list_to_string(delete_empty)


def list_to_string(a_msg):
    # Converts list to a string
    str1 = ""
    return str1.join(a_msg)


def freq_check(message):
    res = {}
    frequencies = []
    for keys in message.lower():
        res[keys] = res.get(keys, 0) + 1
    for value in res.items():
        frequencies.append(value)
    return frequencies


def letters_check(message):
    res = {}
    letters = []
    for keys in message.lower():
        res[keys] = res.get(keys, 0) + 1
    for key in res.items():
        letters.append(key)
    return letters


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=""):
    if isinstance(node, str):
        return {node: binString}
    (left_huff, right_huff) = node.children()
    d_huff = {}
    d_huff.update(huffman_code_tree(left_huff, True, binString + "0"))
    d_huff.update(huffman_code_tree(right_huff, False, binString + "1"))
    return d_huff


if __name__ == "__main__":
    # User's message string
    msg = message_input()

    # User's message string without spaces
    MESSAGE = message_extract(msg)

    # Calculating frequency
    freq = freq_check(MESSAGE)

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    print(" Char | Huffman code ")
    print("----------------------")
    for (char, frequency) in freq:
        print(f"  {char}   |  {huffmanCode[char]}")
