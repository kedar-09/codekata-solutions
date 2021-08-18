import pyhash
bloom=[0]*30
print(bloom)
fnv=pyhash.fnv1_32()
murmur=pyhash.murmur3_32()

dictionary=["Hello","Vegeta","pokemon","meliodas","satoru","zero","independence","lol","postpaid","holiday",
           "module","leo","Arslan","water","erwin","fire","qwerty","random","commas","football","hamon","jojo",
           "moroder","stand"]

#print(dictionary)
for word in dictionary:
    fnv_hash=fnv(word)%30
    murmur_hash=murmur(word)%30
    bloom[fnv_hash]=1
    bloom[murmur_hash]=1

print(bloom)

#new word
#fnv_new=fnv("christmas")%30
#murmur_new=murmur("christmas")%30
#print(fnv_new)
#print(murmur_new)
#print(bloom[fnv_new])
#print(bloom[murmur_new])
#print("^False Positive")

#Already existing word
#fnv_veg=fnv("Vegeta")%30
#murmur_veg=murmur("Vegeta")%30
#print(fnv_veg)
#print(murmur_veg)
#print(bloom[fnv_veg])
#print(bloom[murmur_veg])
#print("^True Prediction")

#Taking a word from the user and checking in the bloom filter
user=input("Enter a word: ")
fnv_user=fnv(user)%30
murmur_user=murmur(user)%30
print(user)
print(fnv_user)
print(murmur_user)
print(bloom[fnv_user])
print(bloom[murmur_user])
if bloom[fnv_user] and bloom[murmur_user]==0:
    print("Word is not present in the bloom filter.")
elif bloom[fnv_user]==0 and bloom[murmur_user]==1:
    print("Word is not present in the bloom filter.")
elif bloom[fnv_user]==1 and bloom[murmur_user]==0:
    print("Word is not present in the bloom filter.")
else:
    print("Word may be present in the bloom filter.")
