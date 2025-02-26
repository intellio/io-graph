# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_ediscovery_search import SecurityEdiscoverySearch


class ByEdiscoverySearchIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/searches/{ediscoverySearch%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoverySearch:
		"""
		Get ediscoverySearch
		Read the properties and relationships of an ediscoverySearch object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverysearch-get?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverysearch-update?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-delete-searches?view=graph-rest-1.0
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



	@property
	def additional_sources(self,
	) -> AdditionalSourcesRequest:
		from .additional_sources import AdditionalSourcesRequest
		return AdditionalSourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def add_to_review_set_operation(self,
	) -> AddToReviewSetOperationRequest:
		from .add_to_review_set_operation import AddToReviewSetOperationRequest
		return AddToReviewSetOperationRequest(self.request_adapter, self.path_parameters)

	@property
	def custodian_sources(self,
	) -> CustodianSourcesRequest:
		from .custodian_sources import CustodianSourcesRequest
		return CustodianSourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def last_estimate_statistics_operation(self,
	) -> LastEstimateStatisticsOperationRequest:
		from .last_estimate_statistics_operation import LastEstimateStatisticsOperationRequest
		return LastEstimateStatisticsOperationRequest(self.request_adapter, self.path_parameters)

	@property
	def security_estimate_statistics(self,
	) -> SecurityEstimateStatisticsRequest:
		from .security_estimate_statistics import SecurityEstimateStatisticsRequest
		return SecurityEstimateStatisticsRequest(self.request_adapter, self.path_parameters)

	@property
	def security_export_report(self,
	) -> SecurityExportReportRequest:
		from .security_export_report import SecurityExportReportRequest
		return SecurityExportReportRequest(self.request_adapter, self.path_parameters)

	@property
	def security_export_result(self,
	) -> SecurityExportResultRequest:
		from .security_export_result import SecurityExportResultRequest
		return SecurityExportResultRequest(self.request_adapter, self.path_parameters)

	@property
	def security_purge_data(self,
	) -> SecurityPurgeDataRequest:
		from .security_purge_data import SecurityPurgeDataRequest
		return SecurityPurgeDataRequest(self.request_adapter, self.path_parameters)

	@property
	def noncustodial_sources(self,
	) -> NoncustodialSourcesRequest:
		from .noncustodial_sources import NoncustodialSourcesRequest
		return NoncustodialSourcesRequest(self.request_adapter, self.path_parameters)

