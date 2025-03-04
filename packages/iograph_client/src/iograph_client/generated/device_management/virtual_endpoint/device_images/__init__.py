# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_source_images import GetSourceImagesRequest
	from .count import CountRequest
	from .by_cloud_pc_device_image_id import ByCloudPcDeviceImageIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.cloud_pc_device_image import CloudPcDeviceImage
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.cloud_pc_device_image_collection_response import CloudPcDeviceImageCollectionResponse


class DeviceImagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/deviceImages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPcDeviceImageCollectionResponse:
		"""
		List deviceImages
		List the properties and relationships of cloudPcDeviceImage objects (operating system images) uploaded to Cloud PC.
		Find more info here: https://learn.microsoft.com/graph/api/virtualendpoint-list-deviceimages?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcDeviceImageCollectionResponse, error_mapping)

	async def post(
		self,
		body: CloudPcDeviceImage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcDeviceImage:
		"""
		Create cloudPcDeviceImage
		Create a new cloudPcDeviceImage object. Upload a custom OS image that you can later provision on Cloud PCs.
		Find more info here: https://learn.microsoft.com/graph/api/virtualendpoint-post-deviceimages?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcDeviceImage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceImagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceImagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceImagesRequest(self.request_adapter, self.path_parameters)

	def by_cloud_pc_device_image_id(self,
		cloudPcDeviceImage_id: str,
	) -> ByCloudPcDeviceImageIdRequest:
		if cloudPcDeviceImage_id is None:
			raise TypeError("cloudPcDeviceImage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcDeviceImage%2Did"] =  cloudPcDeviceImage_id

		from .by_cloud_pc_device_image_id import ByCloudPcDeviceImageIdRequest
		return ByCloudPcDeviceImageIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def get_source_images(self,
	) -> GetSourceImagesRequest:
		from .get_source_images import GetSourceImagesRequest
		return GetSourceImagesRequest(self.request_adapter, self.path_parameters)

