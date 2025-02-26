# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .site_protection_units import SiteProtectionUnitsRequest
	from .site_inclusion_rules import SiteInclusionRulesRequest
	from .share_point_restore_sessions import SharePointRestoreSessionsRequest
	from .share_point_protection_policies import SharePointProtectionPoliciesRequest
	from .service_apps import ServiceAppsRequest
	from .restore_sessions import RestoreSessionsRequest
	from .restore_points import RestorePointsRequest
	from .protection_units import ProtectionUnitsRequest
	from .protection_policies import ProtectionPoliciesRequest
	from .one_drive_for_business_restore_sessions import OneDriveForBusinessRestoreSessionsRequest
	from .one_drive_for_business_protection_policies import OneDriveForBusinessProtectionPoliciesRequest
	from .enable import EnableRequest
	from .mailbox_protection_units import MailboxProtectionUnitsRequest
	from .mailbox_inclusion_rules import MailboxInclusionRulesRequest
	from .exchange_restore_sessions import ExchangeRestoreSessionsRequest
	from .exchange_protection_policies import ExchangeProtectionPoliciesRequest
	from .drive_protection_units import DriveProtectionUnitsRequest
	from .drive_inclusion_rules import DriveInclusionRulesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.backup_restore_root import BackupRestoreRoot


class BackupRestoreRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/solutions/backupRestore"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BackupRestoreRoot:
		"""
		Get backupRestoreRoot
		Get the serviceStatus of the Microsoft 365 Backup Storage service in a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-get?view=graph-rest-1.0
		"""
		tags = ['solutions.backupRestoreRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, BackupRestoreRoot, error_mapping)

	async def patch(
		self,
		body: BackupRestoreRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BackupRestoreRoot:
		"""
		Update the navigation property backupRestore in solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, BackupRestoreRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property backupRestore for solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	@property
	def drive_inclusion_rules(self,
	) -> DriveInclusionRulesRequest:
		from .drive_inclusion_rules import DriveInclusionRulesRequest
		return DriveInclusionRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def drive_protection_units(self,
	) -> DriveProtectionUnitsRequest:
		from .drive_protection_units import DriveProtectionUnitsRequest
		return DriveProtectionUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_protection_policies(self,
	) -> ExchangeProtectionPoliciesRequest:
		from .exchange_protection_policies import ExchangeProtectionPoliciesRequest
		return ExchangeProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_restore_sessions(self,
	) -> ExchangeRestoreSessionsRequest:
		from .exchange_restore_sessions import ExchangeRestoreSessionsRequest
		return ExchangeRestoreSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_inclusion_rules(self,
	) -> MailboxInclusionRulesRequest:
		from .mailbox_inclusion_rules import MailboxInclusionRulesRequest
		return MailboxInclusionRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_protection_units(self,
	) -> MailboxProtectionUnitsRequest:
		from .mailbox_protection_units import MailboxProtectionUnitsRequest
		return MailboxProtectionUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def enable(self,
	) -> EnableRequest:
		from .enable import EnableRequest
		return EnableRequest(self.request_adapter, self.path_parameters)

	@property
	def one_drive_for_business_protection_policies(self,
	) -> OneDriveForBusinessProtectionPoliciesRequest:
		from .one_drive_for_business_protection_policies import OneDriveForBusinessProtectionPoliciesRequest
		return OneDriveForBusinessProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def one_drive_for_business_restore_sessions(self,
	) -> OneDriveForBusinessRestoreSessionsRequest:
		from .one_drive_for_business_restore_sessions import OneDriveForBusinessRestoreSessionsRequest
		return OneDriveForBusinessRestoreSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def protection_policies(self,
	) -> ProtectionPoliciesRequest:
		from .protection_policies import ProtectionPoliciesRequest
		return ProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def protection_units(self,
	) -> ProtectionUnitsRequest:
		from .protection_units import ProtectionUnitsRequest
		return ProtectionUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def restore_points(self,
	) -> RestorePointsRequest:
		from .restore_points import RestorePointsRequest
		return RestorePointsRequest(self.request_adapter, self.path_parameters)

	@property
	def restore_sessions(self,
	) -> RestoreSessionsRequest:
		from .restore_sessions import RestoreSessionsRequest
		return RestoreSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_apps(self,
	) -> ServiceAppsRequest:
		from .service_apps import ServiceAppsRequest
		return ServiceAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def share_point_protection_policies(self,
	) -> SharePointProtectionPoliciesRequest:
		from .share_point_protection_policies import SharePointProtectionPoliciesRequest
		return SharePointProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def share_point_restore_sessions(self,
	) -> SharePointRestoreSessionsRequest:
		from .share_point_restore_sessions import SharePointRestoreSessionsRequest
		return SharePointRestoreSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def site_inclusion_rules(self,
	) -> SiteInclusionRulesRequest:
		from .site_inclusion_rules import SiteInclusionRulesRequest
		return SiteInclusionRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def site_protection_units(self,
	) -> SiteProtectionUnitsRequest:
		from .site_protection_units import SiteProtectionUnitsRequest
		return SiteProtectionUnitsRequest(self.request_adapter, self.path_parameters)

