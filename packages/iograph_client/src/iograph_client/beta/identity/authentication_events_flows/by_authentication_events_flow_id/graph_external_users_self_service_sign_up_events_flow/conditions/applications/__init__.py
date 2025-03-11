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
	from .include_applications import IncludeApplicationsRequest
	from ........request_adapter import HttpxRequestAdapter


class ApplicationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow-id}/graph.externalUsersSelfServiceSignUpEventsFlow/conditions/applications", path_parameters)

	def with_url(self, raw_url: str) -> ApplicationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ApplicationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ApplicationsRequest(self.request_adapter, self.path_parameters)

	def include_applications(self,
		authenticationEventsFlow_id: str,
	) -> IncludeApplicationsRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .include_applications import IncludeApplicationsRequest
		return IncludeApplicationsRequest(self.request_adapter, path_parameters)

