from __future__ import annotations
from enum import StrEnum


class SynchronizationMetadata(StrEnum):
	galleryApplicationIdentifier = "galleryApplicationIdentifier"
	galleryApplicationKey = "galleryApplicationKey"
	isOAuthEnabled = "isOAuthEnabled"
	IsSynchronizationAgentAssignmentRequired = "IsSynchronizationAgentAssignmentRequired"
	isSynchronizationAgentRequired = "isSynchronizationAgentRequired"
	isSynchronizationInPreview = "isSynchronizationInPreview"
	oAuthSettings = "oAuthSettings"
	synchronizationLearnMoreIbizaFwLink = "synchronizationLearnMoreIbizaFwLink"
	configurationFields = "configurationFields"

