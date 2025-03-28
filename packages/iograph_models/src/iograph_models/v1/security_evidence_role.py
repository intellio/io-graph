from __future__ import annotations
from enum import StrEnum


class SecurityEvidenceRole(StrEnum):
	unknown = "unknown"
	contextual = "contextual"
	scanned = "scanned"
	source = "source"
	destination = "destination"
	created = "created"
	added = "added"
	compromised = "compromised"
	edited = "edited"
	attacked = "attacked"
	attacker = "attacker"
	commandAndControl = "commandAndControl"
	loaded = "loaded"
	suspicious = "suspicious"
	policyViolator = "policyViolator"
	unknownFutureValue = "unknownFutureValue"

