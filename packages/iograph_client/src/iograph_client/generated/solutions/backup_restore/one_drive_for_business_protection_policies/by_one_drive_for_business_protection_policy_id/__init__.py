# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .drive_protection_units import DriveProtectionUnitsRequest
	from .drive_inclusion_rules import DriveInclusionRulesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByOneDriveForBusinessProtectionPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessProtectionPolicies/{oneDriveForBusinessProtectionPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OneDriveForBusinessProtectionPolicy:
		"""
		Get oneDriveForBusinessProtectionPolicies from solutions
		The list of OneDrive for Business protection policies in the tenant.
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
		return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicy, error_mapping)

	async def patch(
		self,
		body: OneDriveForBusinessProtectionPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OneDriveForBusinessProtectionPolicy:
		"""
		Update oneDriveForBusinessProtectionPolicy
		Update the protection policy for the OneDrive service in Microsoft 365. This method adds a driveProtectionUnit to or removes it from a oneDriveForBusinessProtectionPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessprotectionpolicy-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property oneDriveForBusinessProtectionPolicies for solutions
		
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



	def with_url(self, raw_url: str) -> ByOneDriveForBusinessProtectionPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOneDriveForBusinessProtectionPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOneDriveForBusinessProtectionPolicyIdRequest(self.request_adapter, self.path_parameters)

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

