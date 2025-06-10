votes = ["A", "B", "A", "C", "B", "A"]  
# Use dictionary to count votes → {"A":3, "B":2, "C":1}  


voteCounter = {'A':0, 'B':0, 'C':0}

for vote in votes:
    voteCounter[vote] +=1
    print(str(voteCounter[vote]) + f' for Candidate: {vote}')  # Describes who got the vote after each vote counted.