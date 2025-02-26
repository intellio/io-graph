from __future__ import annotations
from enum import Enum


class SecurityKubernetesPlatform(Enum):
	unknown = "unknown"
	aks = "aks"
	eks = "eks"
	gke = "gke"
	arc = "arc"
	unknownFutureValue = "unknownFutureValue"

