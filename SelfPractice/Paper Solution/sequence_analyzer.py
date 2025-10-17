class SequenceAnalyzer:
    """Utility class for analyzing numeric sequences."""

    def __init__(self, data):
        self.data = list(data)

    def minmax(self):
        """Return smallest and largest numbers without using min or max."""
        smallest = largest = self.data[0]
        for item in self.data[1:]:
            if item < smallest:
                smallest = item
            elif item > largest:
                largest = item
        return (smallest, largest)

    def sum_of_squares(self):
        """Compute sum of squares using comprehension."""
        return sum([x * x for x in self.data])
    
    """              paper codes                 """
""" yhn sirf numbs ki list change hogai h but data sequenceAnalyzer ka manga h  """
# numbs =[1,2,3]
# s = SequenceAnalyzer(numbs)
# numbs.append(4)
# print(s.data)

# nums = [1, 2, 3]
# s = SequenceAnalyzer(nums)
# nums.append(4)  # Yahan original nums list change ho gayi
# print(numbs)   # Isliye s.data bhi [1, 2, 3, 4] ho gaya


# # numbs = [1, 2, 3]
# # s = SequenceAnalyzer(numbs)
# # numbs.append(4)
# # print(s.data)

# # print(SequenceAnalyzer([1, 2, 3,4]).sum_of_squares())

# analyzer = SequenceAnalyzer([1, 2, 3, 2,3])
# print(analyzer.distinict_count(),analyzer.is_unique())


# analyzer = SequenceAnalyzer([2,4,6])
# print(analyzer.has_odd_product_pair())

# gen = SequenceAnalyzer([1,2,3]).squares_generator()
# next(gen)
# next(gen)
# print(next(gen))

