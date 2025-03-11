from __future__ import annotations
from enum import StrEnum


class EapType(StrEnum):
	eapTls = "eapTls"
	leap = "leap"
	eapSim = "eapSim"
	eapTtls = "eapTtls"
	peap = "peap"
	eapFast = "eapFast"
	teap = "teap"

