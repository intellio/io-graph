# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .include_applications import IncludeApplicationsRequest
	from .......request_adapter import HttpxRequestAdapter


class ApplicationsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow-id}/conditions/applications"
		self.path_parameters: dict[str, Any] = path_parameters

	@property
	def include_applications(self,
	) -> IncludeApplicationsRequest:
		from .include_applications import IncludeApplicationsRequest
		return IncludeApplicationsRequest(self.request_adapter, self.path_parameters)

