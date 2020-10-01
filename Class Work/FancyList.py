# from random import choice 

# class FancyList(list):
#     def append(self, *items):
#         for item in items:
#             super().append(item)

#     def random_item(self):
#         return choice(self)
    
#     def __str__(self):
#         strings = (str(item) for item in self)
            
#         return " ".join(strings)
    

# # listy = FancyList()
# # listy.append(1, 2, 3)

# # print(listy)

# # listy.append(2)
# # print(listy.random_item())

# def threeSum(nums):
#     ans = []
#     set_ans = {}
#     ans_dict = dict()
#     nums.sort()

#     for (index, num) in enumerate(nums, 0):
        
#         target = num * -1
#         left = 0
#         right = len(nums) - 1

#         while left < right and right < len(nums):
#             sum = nums[left] + nums[right]
#             if index == left or nums[left] + nums[right] < target:
#                 left += 1
#             elif index == right or nums[left] + nums[right] > target:
#                 right -= 1
#             elif sum == target: # Found a triplet 
#                 triplet = [num, nums[left], nums[right]]
#                 triplet.sort()
#                 triplet_key = "".join(str(i) for i in triplet)
                
#                 if triplet_key not in ans_dict:
#                     ans_dict[triplet_key] = True
#                     ans.append(triplet)
                    
            
#                 next_sum = nums[left + 1] + nums[right]
#                 if next_sum == target:
#                     left += 1
#                 else:
#                     right -= 1
    
#     return ans

# print(threeSum([-1 ,0, 1, 2, -1, -4]))

# # -4 -1 -1 0 1 2

def action1( **args ):
    print('action1')
    print(args)
def run_this_test(function_name, **args):
    print("run_this_test")
    function_name(f=args['l'])

run_this_test(action1, f='harry', l= 'potter')