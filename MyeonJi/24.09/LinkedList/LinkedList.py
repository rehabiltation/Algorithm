class ListNode:
    def __init__(self, val=0, next=None):
        # 파라미터 안에 val(내가 가질 값), next(화살표방향)
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        # 아무것도 만들어진 게 없다면
        if not self.head:
            # 가리키는 게 없어도 좋으니 우선 생성~
            self.head = ListNode(val, None)
            return

        # 시작점으로 지정~
        node = self.head
        # 다음 점으로 쭉쭉~
        while node.next:
            node = node.next

        # 만들어 준당
        node.next = ListNode(val, None)

ln = LinkedList()
ln.append(3)
ln.append(5)
ln.append(7)

print(ln)