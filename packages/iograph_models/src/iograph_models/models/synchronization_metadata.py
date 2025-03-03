from __future__ import annotations
from enum import Enum


class SynchronizationMetadata(Enum):
	GalleryApplicationIdentifier = "GalleryApplicationIdentifier"
	GalleryApplicationKey = "GalleryApplicationKey"
	IsOAuthEnabled = "IsOAuthEnabled"
	IsSynchronizationAgentAssignmentRequired = "IsSynchronizationAgentAssignmentRequired"
	IsSynchronizationAgentRequired = "IsSynchronizationAgentRequired"
	IsSynchronizationInPreview = "IsSynchronizationInPreview"
	OAuthSettings = "OAuthSettings"
	SynchronizationLearnMoreIbizaFwLink = "SynchronizationLearnMoreIbizaFwLink"
	ConfigurationFields = "ConfigurationFields"

