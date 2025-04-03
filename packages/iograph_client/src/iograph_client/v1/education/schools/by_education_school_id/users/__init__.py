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
	from .count import CountRequest
	from .by_education_user_id import ByEducationUserIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.education_user_collection_response import EducationUserCollectionResponse


class UsersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/schools/{educationSchool%2Did}/users", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationUserCollectionResponse:
		"""
		List users of an educationSchool
		Get the educationUser resources associated with an educationSchool.
		Find more info here: https://learn.microsoft.com/graph/api/educationschool-list-users?view=graph-rest-1.0
		"""
		tags = ['education.educationSchool']

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
		return await self.request_adapter.send_async(request_info, EducationUserCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> UsersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UsersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UsersRequest(self.request_adapter, self.path_parameters)

	@property
	def by_education_user_id(self,
	) -> ByEducationUserIdRequest:
		from .by_education_user_id import ByEducationUserIdRequest
		return ByEducationUserIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		educationSchool_id: str,
	) -> CountRequest:
		if educationSchool_id is None:
			raise TypeError("educationSchool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationSchool%2Did"] =  educationSchool_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		educationSchool_id: str,
	) -> RefRequest:
		if educationSchool_id is None:
			raise TypeError("educationSchool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationSchool%2Did"] =  educationSchool_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

