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
	from .tags import TagsRequest
	from .source_collections import SourceCollectionsRequest
	from .settings import SettingsRequest
	from .review_sets import ReviewSetsRequest
	from .operations import OperationsRequest
	from .noncustodial_data_sources import NoncustodialDataSourcesRequest
	from .ediscovery_reopen import EdiscoveryReopenRequest
	from .ediscovery_close import EdiscoveryCloseRequest
	from .legal_holds import LegalHoldsRequest
	from .custodians import CustodiansRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ediscovery_case import EdiscoveryCase


class ByCaseIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryCase:
		"""
		Get case
		Retrieve the properties and relationships of a case object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoveryCase, error_mapping)

	async def patch(
		self,
		body: EdiscoveryCase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryCase:
		"""
		Update case
		Update the properties of a case object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoveryCase, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete case
		Delete a case object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByCaseIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCaseIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCaseIdRequest(self.request_adapter, self.path_parameters)

	def custodians(self,
		case_id: str,
	) -> CustodiansRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .custodians import CustodiansRequest
		return CustodiansRequest(self.request_adapter, path_parameters)

	def legal_holds(self,
		case_id: str,
	) -> LegalHoldsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .legal_holds import LegalHoldsRequest
		return LegalHoldsRequest(self.request_adapter, path_parameters)

	def ediscovery_close(self,
		case_id: str,
	) -> EdiscoveryCloseRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .ediscovery_close import EdiscoveryCloseRequest
		return EdiscoveryCloseRequest(self.request_adapter, path_parameters)

	def ediscovery_reopen(self,
		case_id: str,
	) -> EdiscoveryReopenRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .ediscovery_reopen import EdiscoveryReopenRequest
		return EdiscoveryReopenRequest(self.request_adapter, path_parameters)

	def noncustodial_data_sources(self,
		case_id: str,
	) -> NoncustodialDataSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .noncustodial_data_sources import NoncustodialDataSourcesRequest
		return NoncustodialDataSourcesRequest(self.request_adapter, path_parameters)

	def operations(self,
		case_id: str,
	) -> OperationsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def review_sets(self,
		case_id: str,
	) -> ReviewSetsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .review_sets import ReviewSetsRequest
		return ReviewSetsRequest(self.request_adapter, path_parameters)

	def settings(self,
		case_id: str,
	) -> SettingsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def source_collections(self,
		case_id: str,
	) -> SourceCollectionsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .source_collections import SourceCollectionsRequest
		return SourceCollectionsRequest(self.request_adapter, path_parameters)

	def tags(self,
		case_id: str,
	) -> TagsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .tags import TagsRequest
		return TagsRequest(self.request_adapter, path_parameters)

