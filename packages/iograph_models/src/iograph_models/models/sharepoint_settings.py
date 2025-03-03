from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class SharepointSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedDomainGuidsForSyncApp: Optional[list[UUID]] = Field(default=None,alias="allowedDomainGuidsForSyncApp",)
	availableManagedPathsForSiteCreation: Optional[list[str]] = Field(default=None,alias="availableManagedPathsForSiteCreation",)
	deletedUserPersonalSiteRetentionPeriodInDays: Optional[int] = Field(default=None,alias="deletedUserPersonalSiteRetentionPeriodInDays",)
	excludedFileExtensionsForSyncApp: Optional[list[str]] = Field(default=None,alias="excludedFileExtensionsForSyncApp",)
	idleSessionSignOut: Optional[IdleSessionSignOut] = Field(default=None,alias="idleSessionSignOut",)
	imageTaggingOption: Optional[ImageTaggingChoice] = Field(default=None,alias="imageTaggingOption",)
	isCommentingOnSitePagesEnabled: Optional[bool] = Field(default=None,alias="isCommentingOnSitePagesEnabled",)
	isFileActivityNotificationEnabled: Optional[bool] = Field(default=None,alias="isFileActivityNotificationEnabled",)
	isLegacyAuthProtocolsEnabled: Optional[bool] = Field(default=None,alias="isLegacyAuthProtocolsEnabled",)
	isLoopEnabled: Optional[bool] = Field(default=None,alias="isLoopEnabled",)
	isMacSyncAppEnabled: Optional[bool] = Field(default=None,alias="isMacSyncAppEnabled",)
	isRequireAcceptingUserToMatchInvitedUserEnabled: Optional[bool] = Field(default=None,alias="isRequireAcceptingUserToMatchInvitedUserEnabled",)
	isResharingByExternalUsersEnabled: Optional[bool] = Field(default=None,alias="isResharingByExternalUsersEnabled",)
	isSharePointMobileNotificationEnabled: Optional[bool] = Field(default=None,alias="isSharePointMobileNotificationEnabled",)
	isSharePointNewsfeedEnabled: Optional[bool] = Field(default=None,alias="isSharePointNewsfeedEnabled",)
	isSiteCreationEnabled: Optional[bool] = Field(default=None,alias="isSiteCreationEnabled",)
	isSiteCreationUIEnabled: Optional[bool] = Field(default=None,alias="isSiteCreationUIEnabled",)
	isSitePagesCreationEnabled: Optional[bool] = Field(default=None,alias="isSitePagesCreationEnabled",)
	isSitesStorageLimitAutomatic: Optional[bool] = Field(default=None,alias="isSitesStorageLimitAutomatic",)
	isSyncButtonHiddenOnPersonalSite: Optional[bool] = Field(default=None,alias="isSyncButtonHiddenOnPersonalSite",)
	isUnmanagedSyncAppForTenantRestricted: Optional[bool] = Field(default=None,alias="isUnmanagedSyncAppForTenantRestricted",)
	personalSiteDefaultStorageLimitInMB: Optional[int] = Field(default=None,alias="personalSiteDefaultStorageLimitInMB",)
	sharingAllowedDomainList: Optional[list[str]] = Field(default=None,alias="sharingAllowedDomainList",)
	sharingBlockedDomainList: Optional[list[str]] = Field(default=None,alias="sharingBlockedDomainList",)
	sharingCapability: Optional[SharingCapabilities] = Field(default=None,alias="sharingCapability",)
	sharingDomainRestrictionMode: Optional[SharingDomainRestrictionMode] = Field(default=None,alias="sharingDomainRestrictionMode",)
	siteCreationDefaultManagedPath: Optional[str] = Field(default=None,alias="siteCreationDefaultManagedPath",)
	siteCreationDefaultStorageLimitInMB: Optional[int] = Field(default=None,alias="siteCreationDefaultStorageLimitInMB",)
	tenantDefaultTimezone: Optional[str] = Field(default=None,alias="tenantDefaultTimezone",)

from .idle_session_sign_out import IdleSessionSignOut
from .image_tagging_choice import ImageTaggingChoice
from .sharing_capabilities import SharingCapabilities
from .sharing_domain_restriction_mode import SharingDomainRestrictionMode

