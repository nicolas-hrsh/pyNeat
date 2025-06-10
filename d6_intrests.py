alice_interests = {"hiking", "chess", "movies"}  
bob_interests = {"chess", "gaming", "cooking"}  


# Find: Shared interests

shared_intrests = {alice_interests & bob_interests}

# Find: Interests unique to Alice

alice_only = {alice_interests - bob_interests}