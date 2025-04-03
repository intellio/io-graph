from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SharepointSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharepointSettings"] = Field(alias="@odata.type", default="#microsoft.graph.sharepointSettings")
	allowedDomainGuidsForSyncApp: Optional[list[UUID]] = Field(alias="allowedDomainGuidsForSyncApp", default=None,)
	availableManagedPathsForSiteCreation: Optional[list[str]] = Field(alias="availableManagedPathsForSiteCreation", default=None,)
	deletedUserPersonalSiteRetentionPeriodInDays: Optional[int] = Field(alias="deletedUserPersonalSiteRetentionPeriodInDays", default=None,)
	excludedFileExtensionsForSyncApp: Optional[list[str]] = Field(alias="excludedFileExtensionsForSyncApp", default=None,)
	idleSessionSignOut: Optional[IdleSessionSignOut] = Field(alias="idleSessionSignOut", default=None,)
	imageTaggingOption: Optional[ImageTaggingChoice | str] = Field(alias="imageTaggingOption", default=None,)
	isCommentingOnSitePagesEnabled: Optional[bool] = Field(alias="isCommentingOnSitePagesEnabled", default=None,)
	isFileActivityNotificationEnabled: Optional[bool] = Field(alias="isFileActivityNotificationEnabled", default=None,)
	isLegacyAuthProtocolsEnabled: Optional[bool] = Field(alias="isLegacyAuthProtocolsEnabled", default=None,)
	isLoopEnabled: Optional[bool] = Field(alias="isLoopEnabled", default=None,)
	isMacSyncAppEnabled: Optional[bool] = Field(alias="isMacSyncAppEnabled", default=None,)
	isRequireAcceptingUserToMatchInvitedUserEnabled: Optional[bool] = Field(alias="isRequireAcceptingUserToMatchInvitedUserEnabled", default=None,)
	isResharingByExternalUsersEnabled: Optional[bool] = Field(alias="isResharingByExternalUsersEnabled", default=None,)
	isSharePointMobileNotificationEnabled: Optional[bool] = Field(alias="isSharePointMobileNotificationEnabled", default=None,)
	isSharePointNewsfeedEnabled: Optional[bool] = Field(alias="isSharePointNewsfeedEnabled", default=None,)
	isSiteCreationEnabled: Optional[bool] = Field(alias="isSiteCreationEnabled", default=None,)
	isSiteCreationUIEnabled: Optional[bool] = Field(alias="isSiteCreationUIEnabled", default=None,)
	isSitePagesCreationEnabled: Optional[bool] = Field(alias="isSitePagesCreationEnabled", default=None,)
	isSitesStorageLimitAutomatic: Optional[bool] = Field(alias="isSitesStorageLimitAutomatic", default=None,)
	isSyncButtonHiddenOnPersonalSite: Optional[bool] = Field(alias="isSyncButtonHiddenOnPersonalSite", default=None,)
	isUnmanagedSyncAppForTenantRestricted: Optional[bool] = Field(alias="isUnmanagedSyncAppForTenantRestricted", default=None,)
	personalSiteDefaultStorageLimitInMB: Optional[int] = Field(alias="personalSiteDefaultStorageLimitInMB", default=None,)
	sharingAllowedDomainList: Optional[list[str]] = Field(alias="sharingAllowedDomainList", default=None,)
	sharingBlockedDomainList: Optional[list[str]] = Field(alias="sharingBlockedDomainList", default=None,)
	sharingCapability: Optional[SharingCapabilities | str] = Field(alias="sharingCapability", default=None,)
	sharingDomainRestrictionMode: Optional[SharingDomainRestrictionMode | str] = Field(alias="sharingDomainRestrictionMode", default=None,)
	siteCreationDefaultManagedPath: Optional[str] = Field(alias="siteCreationDefaultManagedPath", default=None,)
	siteCreationDefaultStorageLimitInMB: Optional[int] = Field(alias="siteCreationDefaultStorageLimitInMB", default=None,)
	tenantDefaultTimezone: Optional[str] = Field(alias="tenantDefaultTimezone", default=None,)

from .idle_session_sign_out import IdleSessionSignOut
from .image_tagging_choice import ImageTaggingChoice
from .sharing_capabilities import SharingCapabilities
from .sharing_domain_restriction_mode import SharingDomainRestrictionMode
