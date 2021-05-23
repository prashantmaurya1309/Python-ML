# nums1=list(map(float,input('enter nums1:').split()))
# nums2=list(map(float,input("enter nums2:").split()))
# sum = len(nums1) + len(nums2)
# merged = []
# l, r = 0, 0
# if sum % 2 != 0:
#             # index = [sum / 2]
#             while (l + r) < (sum / 2):
#                 if nums1[l] < nums2[r]:
#                     merged.append(nums1[l])
#                     l += 1
#                 elif nums1[l] == nums2[r]:
#                     merged.append(nums1[l])
#                     merged.append(nums2[r])
#                     l += 1
#                     r += 1
#                 else:
#                     merged.append(nums2[r])
#                     r += 1
#             print('this is merged',merged)
#             print('median:',merged[-1])
#
# else:
#             # index = [sum / 2, (sum / 2) + 1]
#             while (l + r) < (sum / 2) + 1:
#                 if nums1[l] < nums2[r]:
#                     merged.append(nums1[l])
#                     l += 1
#                 elif nums1[l] == nums2[r]:
#                     merged.append(nums1[l])
#                     merged.append(nums2[r])
#                     l += 1
#                     r += 1
#                 else:
#                     merged.append(nums2[r])
#                     r += 1
#             print('this is merged:',merged)
#             print('median:',(merged[-1] + merged[-2]) / 2)
#
#




m= int(input())
lm = list(map(int,input().split(' ')))
n = int(input())
ln = list(map(int,input().split(' ')))
for i in lm:
    if i in ln:
        ln.remove(i)
    else:
        ln.append(i)

print(ln)
ln1 =set(ln)
for i in sorted(ln1):
    print(i)