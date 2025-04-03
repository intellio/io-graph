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
	from .by_user_configuration_id import ByUserConfigurationIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user_configuration_collection_response import UserConfigurationCollectionResponse


class UserConfigurationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/mailFolders/{mailFolder%2Did}/childFolders/{mailFolder%2Did1}/userConfigurations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserConfigurationCollectionResponse:
		"""
		Get userConfigurations from me
		
		"""
		tags = ['me.mailFolder']

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
		return await self.request_adapter.send_async(request_info, UserConfigurationCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> UserConfigurationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserConfigurationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserConfigurationsRequest(self.request_adapter, self.path_parameters)

	def by_user_configuration_id(self,
		mailFolder_id: str,
		mailFolder_id1: str,
		userConfiguration_id: str,
	) -> ByUserConfigurationIdRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")
		if userConfiguration_id is None:
			raise TypeError("userConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1
		path_parameters["userConfiguration%2Did"] =  userConfiguration_id

		from .by_user_configuration_id import ByUserConfigurationIdRequest
		return ByUserConfigurationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> CountRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

