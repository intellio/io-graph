# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByWindowsInformationProtectionAppLearningSummaryIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsInformationProtectionAppLearningSummaries/{windowsInformationProtectionAppLearningSummary%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsInformationProtectionAppLearningSummary:
		"""
		Get windowsInformationProtectionAppLearningSummary
		Read properties and relationships of the windowsInformationProtectionAppLearningSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-windowsinformationprotectionapplearningsummary-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsInformationProtectionAppLearningSummary']

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
		return await self.request_adapter.send_async(request_info, WindowsInformationProtectionAppLearningSummary, error_mapping)

	async def patch(
		self,
		body: WindowsInformationProtectionAppLearningSummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsInformationProtectionAppLearningSummary:
		"""
		Update windowsInformationProtectionAppLearningSummary
		Update the properties of a windowsInformationProtectionAppLearningSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-windowsinformationprotectionapplearningsummary-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsInformationProtectionAppLearningSummary']

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
		return await self.request_adapter.send_async(request_info, WindowsInformationProtectionAppLearningSummary, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete windowsInformationProtectionAppLearningSummary
		Deletes a windowsInformationProtectionAppLearningSummary.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-windowsinformationprotectionapplearningsummary-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsInformationProtectionAppLearningSummary']
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



	def with_url(self, raw_url: str) -> ByWindowsInformationProtectionAppLearningSummaryIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsInformationProtectionAppLearningSummaryIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsInformationProtectionAppLearningSummaryIdRequest(self.request_adapter, self.path_parameters)

