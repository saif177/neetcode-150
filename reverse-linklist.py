def reverseLinkList(head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

head = [0,1,2,3]
print(reverseLinkList(head))