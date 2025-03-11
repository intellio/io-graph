from __future__ import annotations
from enum import StrEnum


class SimulationAttackTechnique(StrEnum):
	unknown = "unknown"
	credentialHarvesting = "credentialHarvesting"
	attachmentMalware = "attachmentMalware"
	driveByUrl = "driveByUrl"
	linkInAttachment = "linkInAttachment"
	linkToMalwareFile = "linkToMalwareFile"
	unknownFutureValue = "unknownFutureValue"
	oAuthConsentGrant = "oAuthConsentGrant"
	phishTraining = "phishTraining"

