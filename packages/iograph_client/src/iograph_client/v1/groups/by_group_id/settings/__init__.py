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
	from .count import CountRequest
	from .by_group_setting_id import ByGroupSettingIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.group_setting import GroupSetting
from iograph_models.v1.group_setting_collection_response import GroupSettingCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/settings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupSettingCollectionResponse:
		"""
		List settings
		Retrieve a list of tenant-level or group-specific group settings objects.
		Find more info here: https://learn.microsoft.com/graph/api/group-list-settings?view=graph-rest-1.0
		"""
		tags = ['groups.groupSetting']

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
		return await self.request_adapter.send_async(request_info, GroupSettingCollectionResponse, error_mapping)

	async def post(
		self,
		body: GroupSetting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupSetting:
		"""
		Create settings
		Create a new setting based on the templates available in groupSettingTemplates. These settings can be at the tenant-level or at the group level. Group settings apply to only Microsoft 365 groups. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
		Find more info here: https://learn.microsoft.com/graph/api/group-post-settings?view=graph-rest-1.0
		"""
		tags = ['groups.groupSetting']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, GroupSetting, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SettingsRequest(self.request_adapter, self.path_parameters)

	def by_group_setting_id(self,
		group_id: str,
		groupSetting_id: str,
	) -> ByGroupSettingIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if groupSetting_id is None:
			raise TypeError("groupSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["groupSetting%2Did"] =  groupSetting_id

		from .by_group_setting_id import ByGroupSettingIdRequest
		return ByGroupSettingIdRequest(self.request_adapter, path_parameters)

	def count(self,
		group_id: str,
	) -> CountRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

