from __future__ import annotations
from enum import StrEnum


class NetworkaccessIntentCategory(StrEnum):
	initialAccess = "initialAccess"
	persistence = "persistence"
	privilegeEscalation = "privilegeEscalation"
	defenseEvasion = "defenseEvasion"
	credentialAccess = "credentialAccess"
	discovery = "discovery"
	lateralMovement = "lateralMovement"
	execution = "execution"
	collection = "collection"
	exfiltration = "exfiltration"
	commandAndControl = "commandAndControl"
	impact = "impact"
	impairProcessControl = "impairProcessControl"
	inhibitResponseFunction = "inhibitResponseFunction"
	reconnaissance = "reconnaissance"
	resourceDevelopment = "resourceDevelopment"
	evasion = "evasion"
	unknownFutureValue = "unknownFutureValue"

