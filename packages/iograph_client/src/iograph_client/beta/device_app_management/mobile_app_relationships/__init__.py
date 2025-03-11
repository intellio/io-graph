# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_mobile_app_relationship_id import ByMobileAppRelationshipIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.mobile_app_relationship_collection_response import MobileAppRelationshipCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.mobile_app_relationship import MobileAppRelationship


class MobileAppRelationshipsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileAppRelationships", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MobileAppRelationshipCollectionResponse:
		"""
		Get mobileAppRelationships from deviceAppManagement
		List mobileAppRelationship objects for mobile applications.
		"""
		tags = ['deviceAppManagement.mobileAppRelationship']

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
		return await self.request_adapter.send_async(request_info, MobileAppRelationshipCollectionResponse, error_mapping)

	async def post(
		self,
		body: MobileAppRelationship,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MobileAppRelationship:
		"""
		Create new navigation property to mobileAppRelationships for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mobileAppRelationship']

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
		return await self.request_adapter.send_async(request_info, MobileAppRelationship, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MobileAppRelationshipsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MobileAppRelationshipsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MobileAppRelationshipsRequest(self.request_adapter, self.path_parameters)

	def by_mobile_app_relationship_id(self,
		mobileAppRelationship_id: str,
	) -> ByMobileAppRelationshipIdRequest:
		if mobileAppRelationship_id is None:
			raise TypeError("mobileAppRelationship_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileAppRelationship%2Did"] =  mobileAppRelationship_id

		from .by_mobile_app_relationship_id import ByMobileAppRelationshipIdRequest
		return ByMobileAppRelationshipIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

