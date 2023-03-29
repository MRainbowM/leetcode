# https://leetcode.com/problems/defanging-an-ip-address/

"""
1108. Defanging an IP Address

Учитывая действительный (IPv4) IP-адрес address, вернуть защищенную версию этого IP-адреса.

В защищенном IP-адресе  каждая точка заменяется "." на "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


def tests():
    solution = Solution()

    result = solution.defangIPaddr(address="1.1.1.1")
    assert result == "1[.]1[.]1[.]1"

    result = solution.defangIPaddr(address="255.100.50.0")
    assert result == "255[.]100[.]50[.]0"

    print("ВСЕ ЧИКИ-ПУКИ!!!")


tests()
