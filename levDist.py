def levenshteinDistance(string1, string2):
        # Calculate the Levenshtein/Hamming Distance (metric to calculate sentence similairty)
        l1 = len(string1)
        l2 = len(string2)
        lSum = float(l1 + l2)

        distMatrix = {}
        for i in range(-1, l1 + 1):
        	distMatrix[(i, -1)] = i + 1
        for j in range(-1, l2 + 1):
        	distMatrix[(-1, j)] = j + 1
        for i in range(l1):
                for j in range(l2):
                        if string1[i] == string2[j]:
                                cost = 0
                        else:
                                cost = 1

                        insertion = distMatrix[(i,j-1)] + 1
                        deletion = distMatrix[(i-1,j)] + 1
                        substitution = distMatrix[(i-1,j-1)] + cost

                        distMatrix[(i,j)] = min(insertion, deletion, substitution)

                        if i and j and string1[i]==string2[j-1] and string1[i-1] == string2[j]:
                                transposition = distMatrix[i-2,j-2] + cost
                                distMatrix[(i,j)] = min (distMatrix[(i,j)], transposition)

        lDist = distMatrix[l1-1,l2-1]
        ratio = (lSum - lDist)/lSum
        return {'Levenshtein Distance' :lDist, 'Ratio ' :ratio}



print (levenshteinDistance("This is a sample string", "This is a sample string"))
