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
	from .ref import RefRequest
	from ......request_adapter import HttpxRequestAdapter


class ByAppManagementPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application-id}/appManagementPolicies/{appManagementPolicy-id}", path_parameters)

	def with_url(self, raw_url: str) -> ByAppManagementPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAppManagementPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAppManagementPolicyIdRequest(self.request_adapter, self.path_parameters)

	def ref(self,
		application_id: str,
		appManagementPolicy_id: str,
	) -> RefRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if appManagementPolicy_id is None:
			raise TypeError("appManagementPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["appManagementPolicy%2Did"] =  appManagementPolicy_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

