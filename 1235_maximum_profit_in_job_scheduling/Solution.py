import bisect
from typing import List

class Solution:
    # def jobSchedulingRecursive(self, index: int, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     if index >= len(profit) or index <= -1:
    #         return 0
                
    #     # get the next available job
    #     nextAvailable = -1
    #     for jobIndex in range(index, len(profit)):
    #         # print(endTime[jobIndex], startTime[index])
    #         if startTime[jobIndex] >= endTime[index]:
    #             nextAvailable = jobIndex
    #             break
        
    #     return max(
    #         profit[index] + self.jobSchedulingRecursive(nextAvailable, startTime, endTime, profit),
    #         self.jobSchedulingRecursive(index+1, startTime, endTime, profit)
    #     )
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # return self.jobSchedulingRecursive(0, startTime, endTime, profit)
        num_jobs = len(profit)
        maxProfit = [0] * num_jobs
        
        jobs = sorted(zip(startTime, endTime, profit))
        startTime, endTime, profit = zip(*jobs)
        
        print(startTime, endTime, profit)
        
        for index in range(num_jobs-1, -1, -1):
            # get the previous available job
            # for job_index in range(index, num_jobs):
            #     if endTime[index][1] <= jobs[job_index][0]:
            #         previous_available_profit = maxProfit[job_index]
            #         break
            job_index = bisect.bisect_left(startTime, endTime[index])
            previous_available_profit = maxProfit[job_index] if job_index < num_jobs else 0
            
            # print(previous_available_profit, endTime[index])
            
            # get the previous job
            previous_profit = 0
            if index+1 < num_jobs:
                previous_profit = maxProfit[index+1]
                
            # print(previous_profit, previous_available_profit + profit[index])
            
            # select the bigger profit
            maxProfit[index] = max(previous_profit, previous_available_profit + profit[index])
        
        # print(maxProfit)
        
        return maxProfit[0]
        
print(Solution.jobScheduling(Solution, [1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
        