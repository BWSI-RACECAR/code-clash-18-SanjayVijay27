"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""

num_to_word = {0:'twelve', 11:"eleven", 10:"ten", 9:"nine", 8:"eight", 7:"seven", 6:"six", 5:"five", 4:"four", 3:"three", 2:"two", 1:"one"}
ten_to_word = {5:"fifty", 4:"forty", 3:"thirty", 2:"twenty"}
thing_to_word = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 10:"ten"}


    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.
            hour = int(input_time[:2])
            minute = int(input_time[3:])
            a = ""
            minute_word = ""
            if hour >= 12:
                a = " pm"
            else:
                a = " am"
            if minute == 0:
                minute_word = ""
            elif minute <= 9 and minute >= 1:
                minute_word = "oh " + num_to_word[minute]
            elif minute <= 19 and minute >= 10:
                minute_word = thing_to_word[minute]
            elif minute % 10 == 0:
                minute_word = ten_to_word[minute//10]
            else:
                minute_word = ten_to_word[minute//10] + " " + num_to_word[minute%10]
            
            return "It's " + num_to_word[hour % 12] + " " + minute_word + a
            

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        