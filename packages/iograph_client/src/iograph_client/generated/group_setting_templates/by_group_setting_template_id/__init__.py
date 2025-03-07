# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.group_setting_template import GroupSettingTemplate
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByGroupSettingTemplateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groupSettingTemplates/{groupSettingTemplate%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupSettingTemplate:
		"""
		Get a group setting template
		A group setting template represents a template of settings from which settings may be created within a tenant. This operation allows retrieval of the properties of the groupSettingTemplate object, including the available settings and their defaults.
		Find more info here: https://learn.microsoft.com/graph/api/groupsettingtemplate-get?view=graph-rest-1.0
		"""
		tags = ['groupSettingTemplates.groupSettingTemplate']

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
		return await self.request_adapter.send_async(request_info, GroupSettingTemplate, error_mapping)

	async def patch(
		self,
		body: GroupSettingTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupSettingTemplate:
		"""
		Update entity in groupSettingTemplates
		
		"""
		tags = ['groupSettingTemplates.groupSettingTemplate']

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
		return await self.request_adapter.send_async(request_info, GroupSettingTemplate, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from groupSettingTemplates
		
		"""
		tags = ['groupSettingTemplates.groupSettingTemplate']
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



	def with_url(self, raw_url: str) -> ByGroupSettingTemplateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupSettingTemplateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupSettingTemplateIdRequest(self.request_adapter, self.path_parameters)

	def check_member_groups(self,
		groupSettingTemplate_id: str,
	) -> CheckMemberGroupsRequest:
		if groupSettingTemplate_id is None:
			raise TypeError("groupSettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupSettingTemplate%2Did"] =  groupSettingTemplate_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		groupSettingTemplate_id: str,
	) -> CheckMemberObjectsRequest:
		if groupSettingTemplate_id is None:
			raise TypeError("groupSettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupSettingTemplate%2Did"] =  groupSettingTemplate_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		groupSettingTemplate_id: str,
	) -> GetMemberGroupsRequest:
		if groupSettingTemplate_id is None:
			raise TypeError("groupSettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupSettingTemplate%2Did"] =  groupSettingTemplate_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		groupSettingTemplate_id: str,
	) -> GetMemberObjectsRequest:
		if groupSettingTemplate_id is None:
			raise TypeError("groupSettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupSettingTemplate%2Did"] =  groupSettingTemplate_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		groupSettingTemplate_id: str,
	) -> RestoreRequest:
		if groupSettingTemplate_id is None:
			raise TypeError("groupSettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupSettingTemplate%2Did"] =  groupSettingTemplate_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

