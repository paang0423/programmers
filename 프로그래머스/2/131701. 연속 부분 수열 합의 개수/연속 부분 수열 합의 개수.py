def solution(elements):
    hop = set()
    elements = elements + elements
    for i in range(len(elements)//2) :
        for j in range(len(elements)//2) :
            a = sum(elements[j:i+j])
            hop.add(a)
    return len(hop)
