from __future__ import annotations
from enum import StrEnum


class WiredNetworkInterface(StrEnum):
	anyEthernet = "anyEthernet"
	firstActiveEthernet = "firstActiveEthernet"
	secondActiveEthernet = "secondActiveEthernet"
	thirdActiveEthernet = "thirdActiveEthernet"
	firstEthernet = "firstEthernet"
	secondEthernet = "secondEthernet"
	thirdEthernet = "thirdEthernet"

