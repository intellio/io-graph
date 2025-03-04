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
	from .count import CountRequest
	from .by_windows_information_protection_network_learning_summary_id import ByWindowsInformationProtectionNetworkLearningSummaryIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.windows_information_protection_network_learning_summary_collection_response import WindowsInformationProtectionNetworkLearningSummaryCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary


class WindowsInformationProtectionNetworkLearningSummariesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsInformationProtectionNetworkLearningSummaries", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsInformationProtectionNetworkLearningSummaryCollectionResponse:
		"""
		List windowsInformationProtectionNetworkLearningSummaries
		List properties and relationships of the windowsInformationProtectionNetworkLearningSummary objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-windowsinformationprotectionnetworklearningsummary-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsInformationProtectionNetworkLearningSummary']

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
		return await self.request_adapter.send_async(request_info, WindowsInformationProtectionNetworkLearningSummaryCollectionResponse, error_mapping)

	async def post(
		self,
		body: WindowsInformationProtectionNetworkLearningSummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsInformationProtectionNetworkLearningSummary:
		"""
		Create windowsInformationProtectionNetworkLearningSummary
		Create a new windowsInformationProtectionNetworkLearningSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-windowsinformationprotectionnetworklearningsummary-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsInformationProtectionNetworkLearningSummary']

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
		return await self.request_adapter.send_async(request_info, WindowsInformationProtectionNetworkLearningSummary, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> WindowsInformationProtectionNetworkLearningSummariesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: WindowsInformationProtectionNetworkLearningSummariesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return WindowsInformationProtectionNetworkLearningSummariesRequest(self.request_adapter, self.path_parameters)

	def by_windows_information_protection_network_learning_summary_id(self,
		windowsInformationProtectionNetworkLearningSummary_id: str,
	) -> ByWindowsInformationProtectionNetworkLearningSummaryIdRequest:
		if windowsInformationProtectionNetworkLearningSummary_id is None:
			raise TypeError("windowsInformationProtectionNetworkLearningSummary_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsInformationProtectionNetworkLearningSummary%2Did"] =  windowsInformationProtectionNetworkLearningSummary_id

		from .by_windows_information_protection_network_learning_summary_id import ByWindowsInformationProtectionNetworkLearningSummaryIdRequest
		return ByWindowsInformationProtectionNetworkLearningSummaryIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

