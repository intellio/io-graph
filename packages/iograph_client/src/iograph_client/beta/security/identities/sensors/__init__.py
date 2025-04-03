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
	from .security_regenerate_deployment_access_key import SecurityRegenerateDeploymentAccessKeyRequest
	from .security_get_deployment_package_uri import SecurityGetDeploymentPackageUriRequest
	from .security_get_deployment_access_key import SecurityGetDeploymentAccessKeyRequest
	from .count import CountRequest
	from .by_sensor_id import BySensorIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_sensor_collection_response import SecuritySensorCollectionResponse
from iograph_models.beta.security_sensor import SecuritySensor


class SensorsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/identities/sensors", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecuritySensorCollectionResponse:
		"""
		List sensors
		Get a list of sensor objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/security-identitycontainer-list-sensors?view=graph-rest-beta
		"""
		tags = ['security.identityContainer']

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
		return await self.request_adapter.send_async(request_info, SecuritySensorCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecuritySensor,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecuritySensor:
		"""
		Create new navigation property to sensors for security
		
		"""
		tags = ['security.identityContainer']

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
		return await self.request_adapter.send_async(request_info, SecuritySensor, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SensorsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SensorsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SensorsRequest(self.request_adapter, self.path_parameters)

	def by_sensor_id(self,
		sensor_id: str,
	) -> BySensorIdRequest:
		if sensor_id is None:
			raise TypeError("sensor_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sensor%2Did"] =  sensor_id

		from .by_sensor_id import BySensorIdRequest
		return BySensorIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def security_get_deployment_access_key(self,
	) -> SecurityGetDeploymentAccessKeyRequest:
		from .security_get_deployment_access_key import SecurityGetDeploymentAccessKeyRequest
		return SecurityGetDeploymentAccessKeyRequest(self.request_adapter, self.path_parameters)

	@property
	def security_get_deployment_package_uri(self,
	) -> SecurityGetDeploymentPackageUriRequest:
		from .security_get_deployment_package_uri import SecurityGetDeploymentPackageUriRequest
		return SecurityGetDeploymentPackageUriRequest(self.request_adapter, self.path_parameters)

	@property
	def security_regenerate_deployment_access_key(self,
	) -> SecurityRegenerateDeploymentAccessKeyRequest:
		from .security_regenerate_deployment_access_key import SecurityRegenerateDeploymentAccessKeyRequest
		return SecurityRegenerateDeploymentAccessKeyRequest(self.request_adapter, self.path_parameters)

