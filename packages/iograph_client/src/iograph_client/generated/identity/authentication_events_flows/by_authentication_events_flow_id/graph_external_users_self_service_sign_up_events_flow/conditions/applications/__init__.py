# Auto-generated client

from __future__ import annotations
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

	@property
	def include_applications(self,
	) -> IncludeApplicationsRequest:
		from .include_applications import IncludeApplicationsRequest
		return IncludeApplicationsRequest(self.request_adapter, self.path_parameters)

