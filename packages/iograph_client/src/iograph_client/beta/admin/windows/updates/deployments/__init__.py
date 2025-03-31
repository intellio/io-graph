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
	from .count import CountRequest
	from .by_deployment_id import ByDeploymentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_deployment import WindowsUpdatesDeployment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.windows_updates_deployment_collection_response import WindowsUpdatesDeploymentCollectionResponse


class DeploymentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deployments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesDeploymentCollectionResponse:
		"""
		List deployments
		Get a list of deployment objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/adminwindowsupdates-list-deployments?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesDeploymentCollectionResponse, error_mapping)

	async def post(
		self,
		body: WindowsUpdatesDeployment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesDeployment:
		"""
		Create deployment
		Create a new deployment object.
		Find more info here: https://learn.microsoft.com/graph/api/adminwindowsupdates-post-deployments?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesDeployment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeploymentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeploymentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeploymentsRequest(self.request_adapter, self.path_parameters)

	def by_deployment_id(self,
		deployment_id: str,
	) -> ByDeploymentIdRequest:
		if deployment_id is None:
			raise TypeError("deployment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deployment%2Did"] =  deployment_id

		from .by_deployment_id import ByDeploymentIdRequest
		return ByDeploymentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

