# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .unsupported_group_policy_extensions import UnsupportedGroupPolicyExtensionsRequest
	from .update_scope_tags import UpdateScopeTagsRequest
	from .group_policy_setting_mappings import GroupPolicySettingMappingsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_policy_migration_report import GroupPolicyMigrationReport


class ByGroupPolicyMigrationReportIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyMigrationReports/{groupPolicyMigrationReport%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyMigrationReport:
		"""
		Get groupPolicyMigrationReports from deviceManagement
		A list of Group Policy migration reports.
		"""
		tags = ['deviceManagement.groupPolicyMigrationReport']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyMigrationReport, error_mapping)

	async def patch(
		self,
		body: GroupPolicyMigrationReport,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyMigrationReport:
		"""
		Update the navigation property groupPolicyMigrationReports in deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyMigrationReport']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyMigrationReport, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property groupPolicyMigrationReports for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyMigrationReport']
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



	def with_url(self, raw_url: str) -> ByGroupPolicyMigrationReportIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupPolicyMigrationReportIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupPolicyMigrationReportIdRequest(self.request_adapter, self.path_parameters)

	def group_policy_setting_mappings(self,
		groupPolicyMigrationReport_id: str,
	) -> GroupPolicySettingMappingsRequest:
		if groupPolicyMigrationReport_id is None:
			raise TypeError("groupPolicyMigrationReport_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyMigrationReport%2Did"] =  groupPolicyMigrationReport_id

		from .group_policy_setting_mappings import GroupPolicySettingMappingsRequest
		return GroupPolicySettingMappingsRequest(self.request_adapter, path_parameters)

	def update_scope_tags(self,
		groupPolicyMigrationReport_id: str,
	) -> UpdateScopeTagsRequest:
		if groupPolicyMigrationReport_id is None:
			raise TypeError("groupPolicyMigrationReport_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyMigrationReport%2Did"] =  groupPolicyMigrationReport_id

		from .update_scope_tags import UpdateScopeTagsRequest
		return UpdateScopeTagsRequest(self.request_adapter, path_parameters)

	def unsupported_group_policy_extensions(self,
		groupPolicyMigrationReport_id: str,
	) -> UnsupportedGroupPolicyExtensionsRequest:
		if groupPolicyMigrationReport_id is None:
			raise TypeError("groupPolicyMigrationReport_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyMigrationReport%2Did"] =  groupPolicyMigrationReport_id

		from .unsupported_group_policy_extensions import UnsupportedGroupPolicyExtensionsRequest
		return UnsupportedGroupPolicyExtensionsRequest(self.request_adapter, path_parameters)

