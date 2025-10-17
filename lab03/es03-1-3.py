def find_seq(sequence, snippet):
    if snippet in sequence:
        print(f"first instance: [{sequence.index(snippet)}]")
        print(f"no. of instances: {sequence.count(snippet)}")


sequence = "TGCATGCTAGTCAGTTGACA"
snippet = "TAG"

find_seq(sequence, snippet)