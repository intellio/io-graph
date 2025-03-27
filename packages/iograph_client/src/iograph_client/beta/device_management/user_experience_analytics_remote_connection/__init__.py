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
	from .summarize_device_remote_connection_with_summarizeby import SummarizeDeviceRemoteConnectionWithSummarizeByRequest
	from .count import CountRequest
	from .by_user_experience_analytics_remote_connection_id import ByUserExperienceAnalyticsRemoteConnectionIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
from iograph_models.beta.user_experience_analytics_remote_connection_collection_response import UserExperienceAnalyticsRemoteConnectionCollectionResponse


class UserExperienceAnalyticsRemoteConnectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsRemoteConnection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsRemoteConnectionCollectionResponse:
		"""
		Get userExperienceAnalyticsRemoteConnection from deviceManagement
		User experience analytics remote connection. The report will be retired on December 31, 2024. You can start using the Cloud PC connection quality report now via https://learn.microsoft.com/windows-365/enterprise/report-cloud-pc-connection-quality.
		"""
		tags = ['deviceManagement.userExperienceAnalyticsRemoteConnection']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsRemoteConnectionCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsRemoteConnection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsRemoteConnection:
		"""
		Create new navigation property to userExperienceAnalyticsRemoteConnection for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsRemoteConnection']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsRemoteConnection, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserExperienceAnalyticsRemoteConnectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserExperienceAnalyticsRemoteConnectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserExperienceAnalyticsRemoteConnectionRequest(self.request_adapter, self.path_parameters)

	def by_user_experience_analytics_remote_connection_id(self,
		userExperienceAnalyticsRemoteConnection_id: str,
	) -> ByUserExperienceAnalyticsRemoteConnectionIdRequest:
		if userExperienceAnalyticsRemoteConnection_id is None:
			raise TypeError("userExperienceAnalyticsRemoteConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsRemoteConnection%2Did"] =  userExperienceAnalyticsRemoteConnection_id

		from .by_user_experience_analytics_remote_connection_id import ByUserExperienceAnalyticsRemoteConnectionIdRequest
		return ByUserExperienceAnalyticsRemoteConnectionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def summarize_device_remote_connection_with_summarizeby(self,
		summarizeBy: str,
	) -> SummarizeDeviceRemoteConnectionWithSummarizeByRequest:
		if summarizeBy is None:
			raise TypeError("summarizeBy cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["summarizeBy"] =  summarizeBy

		from .summarize_device_remote_connection_with_summarizeby import SummarizeDeviceRemoteConnectionWithSummarizeByRequest
		return SummarizeDeviceRemoteConnectionWithSummarizeByRequest(self.request_adapter, path_parameters)

