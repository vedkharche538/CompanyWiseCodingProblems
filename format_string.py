s = "i.like.this.program.very.much" 
# s = "...home......"
# s = "..geeks..for.geeks."

print('.'.join(list(filter(None, s.split('.')[::-1]))))