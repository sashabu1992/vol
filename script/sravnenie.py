import difflib

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

genuine = [
  "«Братец-хлеб» из Китая носит плащ и корону из булочек, чтобы кормить чаек"
]

plagiary = [
  "Китайский хлебный братец кормит чаек плащом и короной из булочек"
  ]

print(similarity(genuine[0], plagiary[0]))
