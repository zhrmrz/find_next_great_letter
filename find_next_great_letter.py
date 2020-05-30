class Sol:
    def find_next_great_letter(self,arr,char):
        left=0
        right=len(arr)
        while left<right:
            mid=(right+left)//2
            if ord(char)>ord(arr[mid]):
                left=mid+1
            else:
                right=mid
        arr.append(arr[0])
        return arr[left]


if __name__ == '__main__':
    p=Sol()
    print(p.find_next_great_letter(['c','f','j'],'g'))
