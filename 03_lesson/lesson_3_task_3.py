from address import Address
from mailing import Mailing


to_address = Address(555555, "Разумное", "Преображенская", "6", "102")
from_address = Address(222222, "Москва", "Московская", "55", "58")
cost = 1120
track = "postTrack_123456"


mailing = Mailing(track, from_address, to_address, cost)


print(mailing)
