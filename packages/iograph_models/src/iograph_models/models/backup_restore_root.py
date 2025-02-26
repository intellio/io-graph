from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BackupRestoreRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	serviceStatus: Optional[ServiceStatus] = Field(default=None,alias="serviceStatus",)
	driveInclusionRules: list[DriveProtectionRule] = Field(alias="driveInclusionRules",)
	driveProtectionUnits: list[DriveProtectionUnit] = Field(alias="driveProtectionUnits",)
	exchangeProtectionPolicies: list[ExchangeProtectionPolicy] = Field(alias="exchangeProtectionPolicies",)
	exchangeRestoreSessions: list[ExchangeRestoreSession] = Field(alias="exchangeRestoreSessions",)
	mailboxInclusionRules: list[MailboxProtectionRule] = Field(alias="mailboxInclusionRules",)
	mailboxProtectionUnits: list[MailboxProtectionUnit] = Field(alias="mailboxProtectionUnits",)
	oneDriveForBusinessProtectionPolicies: list[OneDriveForBusinessProtectionPolicy] = Field(alias="oneDriveForBusinessProtectionPolicies",)
	oneDriveForBusinessRestoreSessions: list[OneDriveForBusinessRestoreSession] = Field(alias="oneDriveForBusinessRestoreSessions",)
	protectionPolicies: list[ProtectionPolicyBase] = Field(alias="protectionPolicies",)
	protectionUnits: list[ProtectionUnitBase] = Field(alias="protectionUnits",)
	restorePoints: list[RestorePoint] = Field(alias="restorePoints",)
	restoreSessions: list[RestoreSessionBase] = Field(alias="restoreSessions",)
	serviceApps: list[ServiceApp] = Field(alias="serviceApps",)
	sharePointProtectionPolicies: list[SharePointProtectionPolicy] = Field(alias="sharePointProtectionPolicies",)
	sharePointRestoreSessions: list[SharePointRestoreSession] = Field(alias="sharePointRestoreSessions",)
	siteInclusionRules: list[SiteProtectionRule] = Field(alias="siteInclusionRules",)
	siteProtectionUnits: list[SiteProtectionUnit] = Field(alias="siteProtectionUnits",)

from .service_status import ServiceStatus
from .drive_protection_rule import DriveProtectionRule
from .drive_protection_unit import DriveProtectionUnit
from .exchange_protection_policy import ExchangeProtectionPolicy
from .exchange_restore_session import ExchangeRestoreSession
from .mailbox_protection_rule import MailboxProtectionRule
from .mailbox_protection_unit import MailboxProtectionUnit
from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
from .protection_policy_base import ProtectionPolicyBase
from .protection_unit_base import ProtectionUnitBase
from .restore_point import RestorePoint
from .restore_session_base import RestoreSessionBase
from .service_app import ServiceApp
from .share_point_protection_policy import SharePointProtectionPolicy
from .share_point_restore_session import SharePointRestoreSession
from .site_protection_rule import SiteProtectionRule
from .site_protection_unit import SiteProtectionUnit

