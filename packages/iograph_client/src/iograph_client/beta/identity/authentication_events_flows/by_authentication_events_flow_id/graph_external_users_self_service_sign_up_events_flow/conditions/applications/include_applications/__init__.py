# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_authentication_condition_application_app_id import ByAuthenticationConditionApplicationAppIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.authentication_condition_application import AuthenticationConditionApplication
from iograph_models.beta.authentication_condition_application_collection_response import AuthenticationConditionApplicationCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class IncludeApplicationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/conditions/applications/includeApplications", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationConditionApplicationCollectionResponse:
		"""
		Get includeApplications from identity
		
		"""
		tags = ['identity.authenticationEventsFlow']

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
		return await self.request_adapter.send_async(request_info, AuthenticationConditionApplicationCollectionResponse, error_mapping)

	async def post(
		self,
		body: AuthenticationConditionApplication,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationConditionApplication:
		"""
		Create new navigation property to includeApplications for identity
		
		"""
		tags = ['identity.authenticationEventsFlow']

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
		return await self.request_adapter.send_async(request_info, AuthenticationConditionApplication, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> IncludeApplicationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IncludeApplicationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IncludeApplicationsRequest(self.request_adapter, self.path_parameters)

	def by_authentication_condition_application_app_id(self,
		authenticationEventsFlow_id: str,
		authenticationConditionApplication_appId: str,
	) -> ByAuthenticationConditionApplicationAppIdRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")
		if authenticationConditionApplication_appId is None:
			raise TypeError("authenticationConditionApplication_appId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id
		path_parameters["authenticationConditionApplication%2DappId"] =  authenticationConditionApplication_appId

		from .by_authentication_condition_application_app_id import ByAuthenticationConditionApplicationAppIdRequest
		return ByAuthenticationConditionApplicationAppIdRequest(self.request_adapter, path_parameters)

	def count(self,
		authenticationEventsFlow_id: str,
	) -> CountRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

