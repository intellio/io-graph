# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .terms_and_conditions import TermsAndConditionsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus


class ByTermsAndConditionsAcceptanceStatusIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/termsAndConditions/{termsAndConditions%2Did}/acceptanceStatuses/{termsAndConditionsAcceptanceStatus%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermsAndConditionsAcceptanceStatus:
		"""
		Get acceptanceStatuses from deviceManagement
		The list of acceptance statuses for this T&C policy.
		"""
		tags = ['deviceManagement.termsAndConditions']

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
		return await self.request_adapter.send_async(request_info, TermsAndConditionsAcceptanceStatus, error_mapping)

	async def patch(
		self,
		body: TermsAndConditionsAcceptanceStatus,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermsAndConditionsAcceptanceStatus:
		"""
		Update the navigation property acceptanceStatuses in deviceManagement
		
		"""
		tags = ['deviceManagement.termsAndConditions']

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
		return await self.request_adapter.send_async(request_info, TermsAndConditionsAcceptanceStatus, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property acceptanceStatuses for deviceManagement
		
		"""
		tags = ['deviceManagement.termsAndConditions']
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



	def with_url(self, raw_url: str) -> ByTermsAndConditionsAcceptanceStatusIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTermsAndConditionsAcceptanceStatusIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTermsAndConditionsAcceptanceStatusIdRequest(self.request_adapter, self.path_parameters)

	def terms_and_conditions(self,
		termsAndConditions_id: str,
		termsAndConditionsAcceptanceStatus_id: str,
	) -> TermsAndConditionsRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")
		if termsAndConditionsAcceptanceStatus_id is None:
			raise TypeError("termsAndConditionsAcceptanceStatus_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id
		path_parameters["termsAndConditionsAcceptanceStatus%2Did"] =  termsAndConditionsAcceptanceStatus_id

		from .terms_and_conditions import TermsAndConditionsRequest
		return TermsAndConditionsRequest(self.request_adapter, path_parameters)

