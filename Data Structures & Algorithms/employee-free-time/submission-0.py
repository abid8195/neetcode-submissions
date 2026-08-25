class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []

        START = 1
        END = 2

        for employee in schedule:
            for interval in employee:
                events.append((interval.start, START))
                events.append((interval.end, END))
        events.sort()

        ans = []
        current = 0
        start = None

        for x, event in events:
            if current == 0 and start is not None:
                if start < x:
                    ans.append(Interval(start, x))
            
            if event == START:
                current += 1
            else:
                current -= 1
            
            if current == 0:
                start = x
        return ans