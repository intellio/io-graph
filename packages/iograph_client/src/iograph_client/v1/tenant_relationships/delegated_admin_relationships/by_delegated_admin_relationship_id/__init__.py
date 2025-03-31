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
	from .requests import RequestsRequest
	from .operations import OperationsRequest
	from .access_assignments import AccessAssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.delegated_admin_relationship import DelegatedAdminRelationship
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByDelegatedAdminRelationshipIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/delegatedAdminRelationships/{delegatedAdminRelationship%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DelegatedAdminRelationship:
		"""
		Get delegatedAdminRelationship
		Read the properties of a delegatedAdminRelationship object.
		Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DelegatedAdminRelationship, error_mapping)

	async def patch(
		self,
		body: DelegatedAdminRelationship,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DelegatedAdminRelationship:
		"""
		Update delegatedAdminRelationship
		Update the properties of a delegatedAdminRelationship object.  The following restrictions apply:
- You can update this relationship when its status property is created.
- You can update the autoExtendDuration property when status is either created or active.
- You can only remove the Microsoft Entra Global Administrator role when the status property is active, which indicates a long-running operation.
		Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-update?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.delegatedAdminRelationship']

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
		return await self.request_adapter.send_async(request_info, DelegatedAdminRelationship, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete delegatedAdminRelationship
		Delete a delegatedAdminRelationship object. A relationship can only be deleted if it's in the 'created' status. 
		Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-delete?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.delegatedAdminRelationship']
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



	def with_url(self, raw_url: str) -> ByDelegatedAdminRelationshipIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDelegatedAdminRelationshipIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDelegatedAdminRelationshipIdRequest(self.request_adapter, self.path_parameters)

	def access_assignments(self,
		delegatedAdminRelationship_id: str,
	) -> AccessAssignmentsRequest:
		if delegatedAdminRelationship_id is None:
			raise TypeError("delegatedAdminRelationship_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["delegatedAdminRelationship%2Did"] =  delegatedAdminRelationship_id

		from .access_assignments import AccessAssignmentsRequest
		return AccessAssignmentsRequest(self.request_adapter, path_parameters)

	def operations(self,
		delegatedAdminRelationship_id: str,
	) -> OperationsRequest:
		if delegatedAdminRelationship_id is None:
			raise TypeError("delegatedAdminRelationship_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["delegatedAdminRelationship%2Did"] =  delegatedAdminRelationship_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def requests(self,
		delegatedAdminRelationship_id: str,
	) -> RequestsRequest:
		if delegatedAdminRelationship_id is None:
			raise TypeError("delegatedAdminRelationship_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["delegatedAdminRelationship%2Did"] =  delegatedAdminRelationship_id

		from .requests import RequestsRequest
		return RequestsRequest(self.request_adapter, path_parameters)

