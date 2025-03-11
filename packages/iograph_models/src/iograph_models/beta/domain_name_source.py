from __future__ import annotations
from enum import StrEnum


class DomainNameSource(StrEnum):
	fullDomainName = "fullDomainName"
	netBiosDomainName = "netBiosDomainName"

