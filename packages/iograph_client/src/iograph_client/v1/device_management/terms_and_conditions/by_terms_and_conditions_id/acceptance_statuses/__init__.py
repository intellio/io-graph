# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_terms_and_conditions_acceptance_status_id import ByTermsAndConditionsAcceptanceStatusIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.terms_and_conditions_acceptance_status_collection_response import TermsAndConditionsAcceptanceStatusCollectionResponse
from iograph_models.v1.terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AcceptanceStatusesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/termsAndConditions/{termsAndConditions%2Did}/acceptanceStatuses", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermsAndConditionsAcceptanceStatusCollectionResponse:
		"""
		List termsAndConditionsAcceptanceStatuses
		List properties and relationships of the termsAndConditionsAcceptanceStatus objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-companyterms-termsandconditionsacceptancestatus-list?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, TermsAndConditionsAcceptanceStatusCollectionResponse, error_mapping)

	async def post(
		self,
		body: TermsAndConditionsAcceptanceStatus,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermsAndConditionsAcceptanceStatus:
		"""
		Create termsAndConditionsAcceptanceStatus
		Create a new termsAndConditionsAcceptanceStatus object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-companyterms-termsandconditionsacceptancestatus-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.termsAndConditions']

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
		return await self.request_adapter.send_async(request_info, TermsAndConditionsAcceptanceStatus, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AcceptanceStatusesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AcceptanceStatusesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AcceptanceStatusesRequest(self.request_adapter, self.path_parameters)

	def by_terms_and_conditions_acceptance_status_id(self,
		termsAndConditions_id: str,
		termsAndConditionsAcceptanceStatus_id: str,
	) -> ByTermsAndConditionsAcceptanceStatusIdRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")
		if termsAndConditionsAcceptanceStatus_id is None:
			raise TypeError("termsAndConditionsAcceptanceStatus_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id
		path_parameters["termsAndConditionsAcceptanceStatus%2Did"] =  termsAndConditionsAcceptanceStatus_id

		from .by_terms_and_conditions_acceptance_status_id import ByTermsAndConditionsAcceptanceStatusIdRequest
		return ByTermsAndConditionsAcceptanceStatusIdRequest(self.request_adapter, path_parameters)

	def count(self,
		termsAndConditions_id: str,
	) -> CountRequest:
		if termsAndConditions_id is None:
			raise TypeError("termsAndConditions_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["termsAndConditions%2Did"] =  termsAndConditions_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

