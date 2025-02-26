from __future__ import annotations
from enum import Enum


class SimulationAttackTechnique(Enum):
	unknown = "unknown"
	credentialHarvesting = "credentialHarvesting"
	attachmentMalware = "attachmentMalware"
	driveByUrl = "driveByUrl"
	linkInAttachment = "linkInAttachment"
	linkToMalwareFile = "linkToMalwareFile"
	unknownFutureValue = "unknownFutureValue"

