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
	from .by_delegated_admin_relationship_operation_id import ByDelegatedAdminRelationshipOperationIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
from iograph_models.models.delegated_admin_relationship_operation_collection_response import DelegatedAdminRelationshipOperationCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class OperationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/delegatedAdminRelationships/{delegatedAdminRelationship%2Did}/operations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DelegatedAdminRelationshipOperationCollectionResponse:
		"""
		List operations
		Get a list of the delegatedAdminRelationshipOperation objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-list-operations?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.delegatedAdminRelationship']

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
		return await self.request_adapter.send_async(request_info, DelegatedAdminRelationshipOperationCollectionResponse, error_mapping)

	async def post(
		self,
		body: DelegatedAdminRelationshipOperation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DelegatedAdminRelationshipOperation:
		"""
		Create new navigation property to operations for tenantRelationships
		
		"""
		tags = ['tenantRelationships.delegatedAdminRelationship']

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
		return await self.request_adapter.send_async(request_info, DelegatedAdminRelationshipOperation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OperationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OperationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OperationsRequest(self.request_adapter, self.path_parameters)

	def by_delegated_admin_relationship_operation_id(self,
		delegatedAdminRelationship_id: str,
		delegatedAdminRelationshipOperation_id: str,
	) -> ByDelegatedAdminRelationshipOperationIdRequest:
		if delegatedAdminRelationship_id is None:
			raise TypeError("delegatedAdminRelationship_id cannot be null.")
		if delegatedAdminRelationshipOperation_id is None:
			raise TypeError("delegatedAdminRelationshipOperation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["delegatedAdminRelationship%2Did"] =  delegatedAdminRelationship_id
		path_parameters["delegatedAdminRelationshipOperation%2Did"] =  delegatedAdminRelationshipOperation_id

		from .by_delegated_admin_relationship_operation_id import ByDelegatedAdminRelationshipOperationIdRequest
		return ByDelegatedAdminRelationshipOperationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		delegatedAdminRelationship_id: str,
	) -> CountRequest:
		if delegatedAdminRelationship_id is None:
			raise TypeError("delegatedAdminRelationship_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["delegatedAdminRelationship%2Did"] =  delegatedAdminRelationship_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

