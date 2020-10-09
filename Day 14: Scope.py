class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference=0
        for i in range(0,int(_),1):
            for j in range(i,int(_),1):
                diff=abs(int(a[i])-int(a[j]))
                if (self.maximumDifference<diff):
                    self.maximumDifference=diff
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
