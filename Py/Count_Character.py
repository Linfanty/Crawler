import pprint

message = input()
cnt = {}
for zimu in message:
    cnt.setdefault(zimu, 0)
    cnt[zimu] += 1
#print(cnt)

pprint.pprint(cnt)
# print(pprint.pformat(cnt)) # IS EQUAL TO
