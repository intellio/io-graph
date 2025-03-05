from __future__ import annotations
from enum import StrEnum


class SynchronizationMetadata(StrEnum):
	GalleryApplicationIdentifier = "GalleryApplicationIdentifier"
	GalleryApplicationKey = "GalleryApplicationKey"
	IsOAuthEnabled = "IsOAuthEnabled"
	IsSynchronizationAgentAssignmentRequired = "IsSynchronizationAgentAssignmentRequired"
	IsSynchronizationAgentRequired = "IsSynchronizationAgentRequired"
	IsSynchronizationInPreview = "IsSynchronizationInPreview"
	OAuthSettings = "OAuthSettings"
	SynchronizationLearnMoreIbizaFwLink = "SynchronizationLearnMoreIbizaFwLink"
	ConfigurationFields = "ConfigurationFields"

