# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .queries import QueriesRequest
	from .security_export import SecurityExportRequest
	from .security_add_to_review_set import SecurityAddToReviewSetRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByEdiscoveryReviewSetIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/reviewSets/{ediscoveryReviewSet%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryReviewSet:
		"""
		Get ediscoveryReviewSet
		Read the properties and relationships of an ediscoveryReviewSet object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoveryreviewset-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryReviewSet, error_mapping)

	async def patch(
		self,
		body: SecurityEdiscoveryReviewSet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryReviewSet:
		"""
		Update the navigation property reviewSets in security
		
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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryReviewSet, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property reviewSets for security
		
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
	def security_add_to_review_set(self,
	) -> SecurityAddToReviewSetRequest:
		from .security_add_to_review_set import SecurityAddToReviewSetRequest
		return SecurityAddToReviewSetRequest(self.request_adapter, self.path_parameters)

	@property
	def security_export(self,
	) -> SecurityExportRequest:
		from .security_export import SecurityExportRequest
		return SecurityExportRequest(self.request_adapter, self.path_parameters)

	@property
	def queries(self,
	) -> QueriesRequest:
		from .queries import QueriesRequest
		return QueriesRequest(self.request_adapter, self.path_parameters)

