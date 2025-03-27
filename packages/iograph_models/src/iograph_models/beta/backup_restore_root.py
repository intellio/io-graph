from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class BackupRestoreRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	serviceStatus: Optional[ServiceStatus] = Field(alias="serviceStatus", default=None,)
	driveInclusionRules: Optional[list[DriveProtectionRule]] = Field(alias="driveInclusionRules", default=None,)
	driveProtectionUnits: Optional[list[DriveProtectionUnit]] = Field(alias="driveProtectionUnits", default=None,)
	driveProtectionUnitsBulkAdditionJobs: Optional[list[DriveProtectionUnitsBulkAdditionJob]] = Field(alias="driveProtectionUnitsBulkAdditionJobs", default=None,)
	exchangeProtectionPolicies: Optional[list[ExchangeProtectionPolicy]] = Field(alias="exchangeProtectionPolicies", default=None,)
	exchangeRestoreSessions: Optional[list[ExchangeRestoreSession]] = Field(alias="exchangeRestoreSessions", default=None,)
	mailboxInclusionRules: Optional[list[MailboxProtectionRule]] = Field(alias="mailboxInclusionRules", default=None,)
	mailboxProtectionUnits: Optional[list[MailboxProtectionUnit]] = Field(alias="mailboxProtectionUnits", default=None,)
	mailboxProtectionUnitsBulkAdditionJobs: Optional[list[MailboxProtectionUnitsBulkAdditionJob]] = Field(alias="mailboxProtectionUnitsBulkAdditionJobs", default=None,)
	oneDriveForBusinessProtectionPolicies: Optional[list[OneDriveForBusinessProtectionPolicy]] = Field(alias="oneDriveForBusinessProtectionPolicies", default=None,)
	oneDriveForBusinessRestoreSessions: Optional[list[OneDriveForBusinessRestoreSession]] = Field(alias="oneDriveForBusinessRestoreSessions", default=None,)
	protectionPolicies: Optional[list[Annotated[Union[ExchangeProtectionPolicy, OneDriveForBusinessProtectionPolicy, SharePointProtectionPolicy]],Field(discriminator="odata_type")]]] = Field(alias="protectionPolicies", default=None,)
	protectionUnits: Optional[list[Annotated[Union[DriveProtectionUnit, MailboxProtectionUnit, SiteProtectionUnit]],Field(discriminator="odata_type")]]] = Field(alias="protectionUnits", default=None,)
	restorePoints: Optional[list[RestorePoint]] = Field(alias="restorePoints", default=None,)
	restoreSessions: Optional[list[Annotated[Union[ExchangeRestoreSession, OneDriveForBusinessRestoreSession, SharePointRestoreSession]],Field(discriminator="odata_type")]]] = Field(alias="restoreSessions", default=None,)
	serviceApps: Optional[list[ServiceApp]] = Field(alias="serviceApps", default=None,)
	sharePointProtectionPolicies: Optional[list[SharePointProtectionPolicy]] = Field(alias="sharePointProtectionPolicies", default=None,)
	sharePointRestoreSessions: Optional[list[SharePointRestoreSession]] = Field(alias="sharePointRestoreSessions", default=None,)
	siteInclusionRules: Optional[list[SiteProtectionRule]] = Field(alias="siteInclusionRules", default=None,)
	siteProtectionUnits: Optional[list[SiteProtectionUnit]] = Field(alias="siteProtectionUnits", default=None,)
	siteProtectionUnitsBulkAdditionJobs: Optional[list[SiteProtectionUnitsBulkAdditionJob]] = Field(alias="siteProtectionUnitsBulkAdditionJobs", default=None,)

from .service_status import ServiceStatus
from .drive_protection_rule import DriveProtectionRule
from .drive_protection_unit import DriveProtectionUnit
from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
from .exchange_protection_policy import ExchangeProtectionPolicy
from .exchange_restore_session import ExchangeRestoreSession
from .mailbox_protection_rule import MailboxProtectionRule
from .mailbox_protection_unit import MailboxProtectionUnit
from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
from .exchange_protection_policy import ExchangeProtectionPolicy
from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
from .share_point_protection_policy import SharePointProtectionPolicy
from .drive_protection_unit import DriveProtectionUnit
from .mailbox_protection_unit import MailboxProtectionUnit
from .site_protection_unit import SiteProtectionUnit
from .restore_point import RestorePoint
from .exchange_restore_session import ExchangeRestoreSession
from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
from .share_point_restore_session import SharePointRestoreSession
from .service_app import ServiceApp
from .share_point_protection_policy import SharePointProtectionPolicy
from .share_point_restore_session import SharePointRestoreSession
from .site_protection_rule import SiteProtectionRule
from .site_protection_unit import SiteProtectionUnit
from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

