from __future__ import annotations
from enum import Enum


class SecurityKubernetesServiceType(Enum):
	unknown = "unknown"
	clusterIP = "clusterIP"
	externalName = "externalName"
	nodePort = "nodePort"
	loadBalancer = "loadBalancer"
	unknownFutureValue = "unknownFutureValue"

