from __future__ import annotations
from enum import StrEnum


class MicrosoftTunnelDeploymentMode(StrEnum):
	standaloneRootful = "standaloneRootful"
	standaloneRootless = "standaloneRootless"
	podRootful = "podRootful"
	podRootless = "podRootless"
	unknownFutureValue = "unknownFutureValue"

