# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_custom_callout_extension_id import ByCustomCalloutExtensionIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.custom_callout_extension_collection_response import CustomCalloutExtensionCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.custom_callout_extension import CustomCalloutExtension


class CustomWorkflowExtensionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}/customWorkflowExtensions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CustomCalloutExtensionCollectionResponse:
		"""
		List accessPackageCustomWorkflowExtensions
		Get a list of the accessPackageAssignmentRequestWorkflowExtension and accessPackageAssignmentWorkflowExtension objects and their properties. The resulting list includes all the customAccessPackageWorkflowExtension objects for the catalog that the caller has access to read. Each object includes an @odata.type property that indicates whether the object is an  accessPackageAssignmentRequestWorkflowExtension or an accessPackageAssignmentWorkflowExtension.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-list-accesspackagecustomworkflowextensions?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CustomCalloutExtensionCollectionResponse, error_mapping)

	async def post(
		self,
		body: CustomCalloutExtension,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CustomCalloutExtension:
		"""
		Create accessPackageCustomWorkflowExtension
		Create a new accessPackageAssignmentRequestWorkflowExtension or accessPackageAssignmentWorkflowExtension object and add it to an existing accessPackageCatalog object. You must explicitly provide an @odata.type property that indicates whether the object is an  accessPackageAssignmentRequestWorkflowExtension or an accessPackageAssignmentWorkflowExtension.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-post-accesspackagecustomworkflowextensions?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, CustomCalloutExtension, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CustomWorkflowExtensionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CustomWorkflowExtensionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CustomWorkflowExtensionsRequest(self.request_adapter, self.path_parameters)

	def by_custom_callout_extension_id(self,
		accessPackageCatalog_id: str,
		customCalloutExtension_id: str,
	) -> ByCustomCalloutExtensionIdRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")
		if customCalloutExtension_id is None:
			raise TypeError("customCalloutExtension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id
		path_parameters["customCalloutExtension%2Did"] =  customCalloutExtension_id

		from .by_custom_callout_extension_id import ByCustomCalloutExtensionIdRequest
		return ByCustomCalloutExtensionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessPackageCatalog_id: str,
	) -> CountRequest:
		if accessPackageCatalog_id is None:
			raise TypeError("accessPackageCatalog_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageCatalog%2Did"] =  accessPackageCatalog_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

