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
	from .ref import RefRequest
	from ........request_adapter import HttpxRequestAdapter


class ByAccessPackageId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/incompatibleAccessPackages/{accessPackage-id1}", path_parameters)

	def with_url(self, raw_url: str) -> ByAccessPackageId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageId1Request(self.request_adapter, self.path_parameters)

	def ref(self,
		accessPackage_id: str,
		accessPackage_id1: str,
	) -> RefRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackage_id1 is None:
			raise TypeError("accessPackage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackage%2Did1"] =  accessPackage_id1

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

