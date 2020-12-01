# Author: Edmund Aduse Poku
from collections import deque


class Node:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self. output_link = None
        self.accepting_id = -1


class AhoCorasick:
    def __init__(self, word_list):
        self.root = Node()
        self.build_trie(word_list)
        self.build_suffix_and_output_links()

    def build_trie(self, word_list):
        for i in range(len(word_list)):
            curr = self.root
            for character in word_list[i].split():
                curr = curr.children.setdefault(character, Node())
            curr.accepting_id = i

    def build_suffix_and_output_links(self):
        self.root.suffix_link = self.root

        qeu = deque()
        for node in self.root.children.values():
            qeu.append(node)
            node.suffix_link = self.root

        while qeu:
            curr = qeu.popleft()
            print(curr.accepting_id)
            for character, node in curr.children.items():
                temp = curr.suffix_link

                while character not in temp.children.keys() and temp is not self.root:
                    temp = temp.suffix_link

                node.suffix_link = (temp.children.get(character) if character in temp.children.keys() else self.root)

                qeu.append(node)

                curr.output_link = (curr.suffix_link if curr.suffix_link.accepting_id >= 0 else curr.suffix_link.output_link)

    def search_for_words_in_word_list(self, text_input):
        matched_positions = []
        parent = self.root
        for i in range(len(text_input)):
            character = text_input[i]
            if character in parent.children.keys():
                parent = parent.children.get(character)

                if parent.accepting_id >= 0:
                    matched_positions[parent.accepting_id] = i

                temp = parent.output_link
                while temp:
                    matched_positions[temp.accepting_id] = i
                    temp = temp.output_link

            else:
                while parent is not self.root and character not in parent.children.keys():
                    parent = parent.suffix_link

                    if character in parent.children.keys():
                        i -= 1

        return matched_positions


aho = AhoCorasick(["hello, you, he, him, not"])
print(aho.search_for_words_in_word_list("hello"))
