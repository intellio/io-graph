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
	from .group_assignments import GroupAssignmentsRequest
	from .assignments import AssignmentsRequest
	from .acceptance_statuses import AcceptanceStatusesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.terms_and_conditions import TermsAndConditions
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByTermsAndConditionsIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/termsAndConditions/{termsAndConditions%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermsAndConditions:
		"""
		Get termsAndConditions from deviceManagement
		The terms and conditions associated with device management of the company.
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
		return await self.request_adapter.send_async(request_info, TermsAndConditions, error_mapping)

	async def patch(
		self,
		body: TermsAndConditions,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermsAndConditions:
		"""
		Update the navigation property termsAndConditions in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, TermsAndConditions, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property termsAndConditions for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByTermsAndConditionsIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTermsAndConditionsIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTermsAndConditionsIdRequest(self.request_adapter, self.path_parameters)

	def acceptance_statuses(self,
		termsAndConditions_id: str,
	) -> AcceptanceStatusesRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id

		from .acceptance_statuses import AcceptanceStatusesRequest
		return AcceptanceStatusesRequest(self.request_adapter, path_parameters)

	def assignments(self,
		termsAndConditions_id: str,
	) -> AssignmentsRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def group_assignments(self,
		termsAndConditions_id: str,
	) -> GroupAssignmentsRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id

		from .group_assignments import GroupAssignmentsRequest
		return GroupAssignmentsRequest(self.request_adapter, path_parameters)

