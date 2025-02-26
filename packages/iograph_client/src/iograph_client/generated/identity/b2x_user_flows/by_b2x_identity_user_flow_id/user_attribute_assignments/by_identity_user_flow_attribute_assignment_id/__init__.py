# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_attribute import UserAttributeRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment


class ByIdentityUserFlowAttributeAssignmentIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/userAttributeAssignments/{identityUserFlowAttributeAssignment%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityUserFlowAttributeAssignment:
		"""
		Get identityUserFlowAttributeAssignment
		Read the properties and relationships of an identityUserFlowAttributeAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/identityuserflowattributeassignment-get?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttributeAssignment, error_mapping)

	async def patch(
		self,
		body: IdentityUserFlowAttributeAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityUserFlowAttributeAssignment:
		"""
		Update identityUserFlowAttributeAssignment
		Update the properties of a identityUserFlowAttributeAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/identityuserflowattributeassignment-update?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityUserFlowAttributeAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete userAttributeAssignment
		Delete an identityUserFlowAttributeAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/identityuserflowattributeassignment-delete?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']
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
	def user_attribute(self,
	) -> UserAttributeRequest:
		from .user_attribute import UserAttributeRequest
		return UserAttributeRequest(self.request_adapter, self.path_parameters)

