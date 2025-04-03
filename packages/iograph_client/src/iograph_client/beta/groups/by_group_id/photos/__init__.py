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
	from .by_profile_photo_id import ByProfilePhotoIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.profile_photo_collection_response import ProfilePhotoCollectionResponse


class PhotosRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/photos", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ProfilePhotoCollectionResponse:
		"""
		List photos
		Retrieve a list of profilePhoto objects.
		Find more info here: https://learn.microsoft.com/graph/api/group-list-photos?view=graph-rest-beta
		"""
		tags = ['groups.profilePhoto']

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
		return await self.request_adapter.send_async(request_info, ProfilePhotoCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> PhotosRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PhotosRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PhotosRequest(self.request_adapter, self.path_parameters)

	def by_profile_photo_id(self,
		group_id: str,
		profilePhoto_id: str,
	) -> ByProfilePhotoIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if profilePhoto_id is None:
			raise TypeError("profilePhoto_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["profilePhoto%2Did"] =  profilePhoto_id

		from .by_profile_photo_id import ByProfilePhotoIdRequest
		return ByProfilePhotoIdRequest(self.request_adapter, path_parameters)

