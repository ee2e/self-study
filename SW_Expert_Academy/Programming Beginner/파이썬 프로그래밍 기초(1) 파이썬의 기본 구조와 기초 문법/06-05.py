s = input()

if s == s.upper() :
    s_s = s.lower()
else :
    s_s = s.upper()

print(f'{s}(ASCII: {ord(s)}) => {s_s}(ASCII: {ord(s_s)})')