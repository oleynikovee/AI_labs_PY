class ValueInt:
    def validation(self,array,type):
        if 0==type:
            array.sort()
        elif 1==type:
            array.sort()
            array.reverse()
        for i in array:
            try:
                int(i)
            except ValueError:
                return False
        return True
        
