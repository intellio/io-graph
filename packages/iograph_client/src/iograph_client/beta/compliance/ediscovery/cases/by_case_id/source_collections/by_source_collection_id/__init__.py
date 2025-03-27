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
	from .ediscovery_purge_data import EdiscoveryPurgeDataRequest
	from .ediscovery_estimate_statistics import EdiscoveryEstimateStatisticsRequest
	from .last_estimate_statistics_operation import LastEstimateStatisticsOperationRequest
	from .custodian_sources import CustodianSourcesRequest
	from .add_to_review_set_operation import AddToReviewSetOperationRequest
	from .additional_sources import AdditionalSourcesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ediscovery_source_collection import EdiscoverySourceCollection


class BySourceCollectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/sourceCollections/{sourceCollection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoverySourceCollection:
		"""
		Get sourceCollections from compliance
		Returns a list of sourceCollection objects associated with this case.
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoverySourceCollection, error_mapping)

	async def patch(
		self,
		body: EdiscoverySourceCollection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoverySourceCollection:
		"""
		Update sourceCollection
		Update the properties of a sourceCollection object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-sourcecollection-update?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoverySourceCollection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete sourceCollection
		Delete a sourceCollection object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-sourcecollection-delete?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']
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



	def with_url(self, raw_url: str) -> BySourceCollectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySourceCollectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySourceCollectionIdRequest(self.request_adapter, self.path_parameters)

	def additional_sources(self,
		case_id: str,
		sourceCollection_id: str,
	) -> AdditionalSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .additional_sources import AdditionalSourcesRequest
		return AdditionalSourcesRequest(self.request_adapter, path_parameters)

	def add_to_review_set_operation(self,
		case_id: str,
		sourceCollection_id: str,
	) -> AddToReviewSetOperationRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .add_to_review_set_operation import AddToReviewSetOperationRequest
		return AddToReviewSetOperationRequest(self.request_adapter, path_parameters)

	def custodian_sources(self,
		case_id: str,
		sourceCollection_id: str,
	) -> CustodianSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .custodian_sources import CustodianSourcesRequest
		return CustodianSourcesRequest(self.request_adapter, path_parameters)

	def last_estimate_statistics_operation(self,
		case_id: str,
		sourceCollection_id: str,
	) -> LastEstimateStatisticsOperationRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .last_estimate_statistics_operation import LastEstimateStatisticsOperationRequest
		return LastEstimateStatisticsOperationRequest(self.request_adapter, path_parameters)

	def ediscovery_estimate_statistics(self,
		case_id: str,
		sourceCollection_id: str,
	) -> EdiscoveryEstimateStatisticsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .ediscovery_estimate_statistics import EdiscoveryEstimateStatisticsRequest
		return EdiscoveryEstimateStatisticsRequest(self.request_adapter, path_parameters)

	def ediscovery_purge_data(self,
		case_id: str,
		sourceCollection_id: str,
	) -> EdiscoveryPurgeDataRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .ediscovery_purge_data import EdiscoveryPurgeDataRequest
		return EdiscoveryPurgeDataRequest(self.request_adapter, path_parameters)

	def noncustodial_sources(self,
		case_id: str,
		sourceCollection_id: str,
	) -> NoncustodialSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if sourceCollection_id is None:
			raise TypeError("sourceCollection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["sourceCollection%2Did"] =  sourceCollection_id

		from .noncustodial_sources import NoncustodialSourcesRequest
		return NoncustodialSourcesRequest(self.request_adapter, path_parameters)

