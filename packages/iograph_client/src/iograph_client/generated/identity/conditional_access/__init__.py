# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .templates import TemplatesRequest
	from .policies import PoliciesRequest
	from .named_locations import NamedLocationsRequest
	from .authentication_strength import AuthenticationStrengthRequest
	from .authentication_context_class_references import AuthenticationContextClassReferencesRequest
	from ....request_adapter import HttpxRequestAdapter


class ConditionalAccessRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/conditionalAccess"
		self.path_parameters: dict[str, Any] = path_parameters

	@property
	def authentication_context_class_references(self,
	) -> AuthenticationContextClassReferencesRequest:
		from .authentication_context_class_references import AuthenticationContextClassReferencesRequest
		return AuthenticationContextClassReferencesRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_strength(self,
	) -> AuthenticationStrengthRequest:
		from .authentication_strength import AuthenticationStrengthRequest
		return AuthenticationStrengthRequest(self.request_adapter, self.path_parameters)

	@property
	def named_locations(self,
	) -> NamedLocationsRequest:
		from .named_locations import NamedLocationsRequest
		return NamedLocationsRequest(self.request_adapter, self.path_parameters)

	@property
	def policies(self,
	) -> PoliciesRequest:
		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def templates(self,
	) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

