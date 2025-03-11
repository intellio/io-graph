# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .custom_extension import CustomExtensionRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.custom_extension_handler import CustomExtensionHandler
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCustomExtensionHandlerIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackage/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy%2Did}/customExtensionHandlers/{customExtensionHandler%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CustomExtensionHandler:
		"""
		Get customExtensionHandlers from identityGovernance
		The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, CustomExtensionHandler, error_mapping)

	async def patch(
		self,
		body: CustomExtensionHandler,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CustomExtensionHandler:
		"""
		Update the navigation property customExtensionHandlers in identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, CustomExtensionHandler, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property customExtensionHandlers for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']
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



	def with_url(self, raw_url: str) -> ByCustomExtensionHandlerIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCustomExtensionHandlerIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCustomExtensionHandlerIdRequest(self.request_adapter, self.path_parameters)

	def custom_extension(self,
		accessPackageAssignment_id: str,
		accessPackageAssignmentPolicy_id: str,
		customExtensionHandler_id: str,
	) -> CustomExtensionRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")
		if customExtensionHandler_id is None:
			raise TypeError("customExtensionHandler_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id
		path_parameters["customExtensionHandler%2Did"] =  customExtensionHandler_id

		from .custom_extension import CustomExtensionRequest
		return CustomExtensionRequest(self.request_adapter, path_parameters)

