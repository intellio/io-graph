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
	from .count import CountRequest
	from .by_access_package_id import ByAccessPackageIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_collection_response import AccessPackageCollectionResponse


class AccessPackagesIncompatibleWithRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackage/accessPackagesIncompatibleWith", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageCollectionResponse:
		"""
		Get accessPackagesIncompatibleWith from identityGovernance
		The access packages that are incompatible with this package. Read-only.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> AccessPackagesIncompatibleWithRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AccessPackagesIncompatibleWithRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AccessPackagesIncompatibleWithRequest(self.request_adapter, self.path_parameters)

	def by_access_package_id(self,
		accessPackageAssignment_id: str,
		accessPackage_id: str,
	) -> ByAccessPackageIdRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .by_access_package_id import ByAccessPackageIdRequest
		return ByAccessPackageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessPackageAssignment_id: str,
	) -> CountRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

