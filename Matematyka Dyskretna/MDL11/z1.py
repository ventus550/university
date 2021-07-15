def source(M):
    vertex = 0;
    for col in range(1, len(M)):
        if M[vertex][col] == 0:
            vertex = col

    #Sprawdzam czy vertex jest źródłem
    if M[vertex][vertex] == 1:
        return False
    for i in range(len(M)):
        if (M[vertex][i] == 0 or M[i][vertex] == 1) and vertex != i:
            return False
    return vertex
















