from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BackupRestoreRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	serviceStatus: Optional[ServiceStatus] = Field(default=None,alias="serviceStatus",)
	driveInclusionRules: Optional[list[DriveProtectionRule]] = Field(default=None,alias="driveInclusionRules",)
	driveProtectionUnits: Optional[list[DriveProtectionUnit]] = Field(default=None,alias="driveProtectionUnits",)
	exchangeProtectionPolicies: Optional[list[ExchangeProtectionPolicy]] = Field(default=None,alias="exchangeProtectionPolicies",)
	exchangeRestoreSessions: Optional[list[ExchangeRestoreSession]] = Field(default=None,alias="exchangeRestoreSessions",)
	mailboxInclusionRules: Optional[list[MailboxProtectionRule]] = Field(default=None,alias="mailboxInclusionRules",)
	mailboxProtectionUnits: Optional[list[MailboxProtectionUnit]] = Field(default=None,alias="mailboxProtectionUnits",)
	oneDriveForBusinessProtectionPolicies: Optional[list[OneDriveForBusinessProtectionPolicy]] = Field(default=None,alias="oneDriveForBusinessProtectionPolicies",)
	oneDriveForBusinessRestoreSessions: Optional[list[OneDriveForBusinessRestoreSession]] = Field(default=None,alias="oneDriveForBusinessRestoreSessions",)
	protectionPolicies: SerializeAsAny[Optional[list[ProtectionPolicyBase]]] = Field(default=None,alias="protectionPolicies",)
	protectionUnits: SerializeAsAny[Optional[list[ProtectionUnitBase]]] = Field(default=None,alias="protectionUnits",)
	restorePoints: Optional[list[RestorePoint]] = Field(default=None,alias="restorePoints",)
	restoreSessions: SerializeAsAny[Optional[list[RestoreSessionBase]]] = Field(default=None,alias="restoreSessions",)
	serviceApps: Optional[list[ServiceApp]] = Field(default=None,alias="serviceApps",)
	sharePointProtectionPolicies: Optional[list[SharePointProtectionPolicy]] = Field(default=None,alias="sharePointProtectionPolicies",)
	sharePointRestoreSessions: Optional[list[SharePointRestoreSession]] = Field(default=None,alias="sharePointRestoreSessions",)
	siteInclusionRules: Optional[list[SiteProtectionRule]] = Field(default=None,alias="siteInclusionRules",)
	siteProtectionUnits: Optional[list[SiteProtectionUnit]] = Field(default=None,alias="siteProtectionUnits",)

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

