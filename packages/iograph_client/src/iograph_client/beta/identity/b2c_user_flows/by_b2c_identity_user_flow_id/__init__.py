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
	from .user_flow_identity_providers import UserFlowIdentityProvidersRequest
	from .user_attribute_assignments import UserAttributeAssignmentsRequest
	from .languages import LanguagesRequest
	from .identity_providers import IdentityProvidersRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.b2c_identity_user_flow import B2cIdentityUserFlow


class ByB2cIdentityUserFlowIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> B2cIdentityUserFlow:
		"""
		Get b2cIdentityUserFlow
		Retrieve the properties and relationships of a b2cUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/b2cidentityuserflow-get?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, B2cIdentityUserFlow, error_mapping)

	async def patch(
		self,
		body: B2cIdentityUserFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> B2cIdentityUserFlow:
		"""
		Update b2cIdentityUserFlow
		Update the properties of a b2cIdentityUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/b2cidentityuserflow-update?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, B2cIdentityUserFlow, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete b2cIdentityUserFlow
		Delete a b2cIdentityUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/b2cidentityuserflow-delete?view=graph-rest-beta
		"""
		tags = ['identity.b2cIdentityUserFlow']
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



	def with_url(self, raw_url: str) -> ByB2cIdentityUserFlowIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByB2cIdentityUserFlowIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByB2cIdentityUserFlowIdRequest(self.request_adapter, self.path_parameters)

	def identity_providers(self,
		b2cIdentityUserFlow_id: str,
	) -> IdentityProvidersRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, path_parameters)

	def languages(self,
		b2cIdentityUserFlow_id: str,
	) -> LanguagesRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .languages import LanguagesRequest
		return LanguagesRequest(self.request_adapter, path_parameters)

	def user_attribute_assignments(self,
		b2cIdentityUserFlow_id: str,
	) -> UserAttributeAssignmentsRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .user_attribute_assignments import UserAttributeAssignmentsRequest
		return UserAttributeAssignmentsRequest(self.request_adapter, path_parameters)

	def user_flow_identity_providers(self,
		b2cIdentityUserFlow_id: str,
	) -> UserFlowIdentityProvidersRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .user_flow_identity_providers import UserFlowIdentityProvidersRequest
		return UserFlowIdentityProvidersRequest(self.request_adapter, path_parameters)

