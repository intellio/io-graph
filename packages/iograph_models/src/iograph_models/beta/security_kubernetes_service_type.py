from __future__ import annotations
from enum import StrEnum


class SecurityKubernetesServiceType(StrEnum):
	unknown = "unknown"
	clusterIP = "clusterIP"
	externalName = "externalName"
	nodePort = "nodePort"
	loadBalancer = "loadBalancer"
	unknownFutureValue = "unknownFutureValue"

