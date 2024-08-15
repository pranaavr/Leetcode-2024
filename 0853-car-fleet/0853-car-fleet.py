class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        fleets = []
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        for car in cars:
            ttd = (target - car[0])/car[1]
            if not fleets or ttd > fleets[-1]:
                fleets.append(ttd)
        
        return len(fleets)
