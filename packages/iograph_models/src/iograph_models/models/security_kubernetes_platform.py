from __future__ import annotations
from enum import StrEnum


class SecurityKubernetesPlatform(StrEnum):
	unknown = "unknown"
	aks = "aks"
	eks = "eks"
	gke = "gke"
	arc = "arc"
	unknownFutureValue = "unknownFutureValue"

