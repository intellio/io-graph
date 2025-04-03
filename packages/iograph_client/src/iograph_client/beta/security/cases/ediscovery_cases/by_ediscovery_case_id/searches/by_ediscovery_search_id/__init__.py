# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .noncustodial_sources import NoncustodialSourcesRequest
	from .security_purge_data import SecurityPurgeDataRequest
	from .security_export_result import SecurityExportResultRequest
	from .security_export_report import SecurityExportReportRequest
	from .security_estimate_statistics import SecurityEstimateStatisticsRequest
	from .last_estimate_statistics_operation import LastEstimateStatisticsOperationRequest
	from .custodian_sources import CustodianSourcesRequest
	from .add_to_review_set_operation import AddToReviewSetOperationRequest
	from .additional_sources import AdditionalSourcesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_ediscovery_search import SecurityEdiscoverySearch


class ByEdiscoverySearchIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/searches/{ediscoverySearch%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoverySearch:
		"""
		Get ediscoverySearch
		Read the properties and relationships of an ediscoverySearch object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverysearch-get?view=graph-rest-beta
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoverySearch, error_mapping)

	async def patch(
		self,
		body: SecurityEdiscoverySearch,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoverySearch:
		"""
		Update ediscoverySearch
		Update the properties of an ediscoverySearch object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverysearch-update?view=graph-rest-beta
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoverySearch, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete ediscoverySearch
		Delete an ediscoverySearch object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-delete-searches?view=graph-rest-beta
		"""
		tags = ['security.casesRoot']
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



	def with_url(self, raw_url: str) -> ByEdiscoverySearchIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEdiscoverySearchIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEdiscoverySearchIdRequest(self.request_adapter, self.path_parameters)

	def additional_sources(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> AdditionalSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .additional_sources import AdditionalSourcesRequest
		return AdditionalSourcesRequest(self.request_adapter, path_parameters)

	def add_to_review_set_operation(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> AddToReviewSetOperationRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .add_to_review_set_operation import AddToReviewSetOperationRequest
		return AddToReviewSetOperationRequest(self.request_adapter, path_parameters)

	def custodian_sources(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> CustodianSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .custodian_sources import CustodianSourcesRequest
		return CustodianSourcesRequest(self.request_adapter, path_parameters)

	def last_estimate_statistics_operation(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> LastEstimateStatisticsOperationRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .last_estimate_statistics_operation import LastEstimateStatisticsOperationRequest
		return LastEstimateStatisticsOperationRequest(self.request_adapter, path_parameters)

	def security_estimate_statistics(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> SecurityEstimateStatisticsRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .security_estimate_statistics import SecurityEstimateStatisticsRequest
		return SecurityEstimateStatisticsRequest(self.request_adapter, path_parameters)

	def security_export_report(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> SecurityExportReportRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .security_export_report import SecurityExportReportRequest
		return SecurityExportReportRequest(self.request_adapter, path_parameters)

	def security_export_result(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> SecurityExportResultRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .security_export_result import SecurityExportResultRequest
		return SecurityExportResultRequest(self.request_adapter, path_parameters)

	def security_purge_data(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> SecurityPurgeDataRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .security_purge_data import SecurityPurgeDataRequest
		return SecurityPurgeDataRequest(self.request_adapter, path_parameters)

	def noncustodial_sources(self,
		ediscoveryCase_id: str,
		ediscoverySearch_id: str,
	) -> NoncustodialSourcesRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoverySearch_id is None:
			raise TypeError("ediscoverySearch_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoverySearch%2Did"] =  ediscoverySearch_id

		from .noncustodial_sources import NoncustodialSourcesRequest
		return NoncustodialSourcesRequest(self.request_adapter, path_parameters)

