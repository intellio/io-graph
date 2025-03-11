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
	from .websites import WebsitesRequest
	from .web_accounts import WebAccountsRequest
	from .skills import SkillsRequest
	from .publications import PublicationsRequest
	from .projects import ProjectsRequest
	from .positions import PositionsRequest
	from .phones import PhonesRequest
	from .patents import PatentsRequest
	from .notes import NotesRequest
	from .names import NamesRequest
	from .languages import LanguagesRequest
	from .interests import InterestsRequest
	from .emails import EmailsRequest
	from .educational_activities import EducationalActivitiesRequest
	from .certifications import CertificationsRequest
	from .awards import AwardsRequest
	from .anniversaries import AnniversariesRequest
	from .addresses import AddressesRequest
	from .account import AccountRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.profile import Profile


class ProfileRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/profile", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Profile:
		"""
		Get profile from users
		Represents properties that are descriptive of a user in a tenant.
		"""
		tags = ['users.profile']

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
		return await self.request_adapter.send_async(request_info, Profile, error_mapping)

	async def patch(
		self,
		body: Profile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Profile:
		"""
		Update the navigation property profile in users
		
		"""
		tags = ['users.profile']

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
		return await self.request_adapter.send_async(request_info, Profile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property profile for users
		
		"""
		tags = ['users.profile']
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



	def with_url(self, raw_url: str) -> ProfileRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ProfileRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ProfileRequest(self.request_adapter, self.path_parameters)

	def account(self,
		user_id: str,
	) -> AccountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .account import AccountRequest
		return AccountRequest(self.request_adapter, path_parameters)

	def addresses(self,
		user_id: str,
	) -> AddressesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .addresses import AddressesRequest
		return AddressesRequest(self.request_adapter, path_parameters)

	def anniversaries(self,
		user_id: str,
	) -> AnniversariesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .anniversaries import AnniversariesRequest
		return AnniversariesRequest(self.request_adapter, path_parameters)

	def awards(self,
		user_id: str,
	) -> AwardsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .awards import AwardsRequest
		return AwardsRequest(self.request_adapter, path_parameters)

	def certifications(self,
		user_id: str,
	) -> CertificationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .certifications import CertificationsRequest
		return CertificationsRequest(self.request_adapter, path_parameters)

	def educational_activities(self,
		user_id: str,
	) -> EducationalActivitiesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .educational_activities import EducationalActivitiesRequest
		return EducationalActivitiesRequest(self.request_adapter, path_parameters)

	def emails(self,
		user_id: str,
	) -> EmailsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .emails import EmailsRequest
		return EmailsRequest(self.request_adapter, path_parameters)

	def interests(self,
		user_id: str,
	) -> InterestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .interests import InterestsRequest
		return InterestsRequest(self.request_adapter, path_parameters)

	def languages(self,
		user_id: str,
	) -> LanguagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .languages import LanguagesRequest
		return LanguagesRequest(self.request_adapter, path_parameters)

	def names(self,
		user_id: str,
	) -> NamesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .names import NamesRequest
		return NamesRequest(self.request_adapter, path_parameters)

	def notes(self,
		user_id: str,
	) -> NotesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .notes import NotesRequest
		return NotesRequest(self.request_adapter, path_parameters)

	def patents(self,
		user_id: str,
	) -> PatentsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .patents import PatentsRequest
		return PatentsRequest(self.request_adapter, path_parameters)

	def phones(self,
		user_id: str,
	) -> PhonesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .phones import PhonesRequest
		return PhonesRequest(self.request_adapter, path_parameters)

	def positions(self,
		user_id: str,
	) -> PositionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .positions import PositionsRequest
		return PositionsRequest(self.request_adapter, path_parameters)

	def projects(self,
		user_id: str,
	) -> ProjectsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .projects import ProjectsRequest
		return ProjectsRequest(self.request_adapter, path_parameters)

	def publications(self,
		user_id: str,
	) -> PublicationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .publications import PublicationsRequest
		return PublicationsRequest(self.request_adapter, path_parameters)

	def skills(self,
		user_id: str,
	) -> SkillsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .skills import SkillsRequest
		return SkillsRequest(self.request_adapter, path_parameters)

	def web_accounts(self,
		user_id: str,
	) -> WebAccountsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .web_accounts import WebAccountsRequest
		return WebAccountsRequest(self.request_adapter, path_parameters)

	def websites(self,
		user_id: str,
	) -> WebsitesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .websites import WebsitesRequest
		return WebsitesRequest(self.request_adapter, path_parameters)

