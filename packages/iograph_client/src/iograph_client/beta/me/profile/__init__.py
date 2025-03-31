# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
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
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.profile import Profile
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ProfileRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/profile", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Profile:
		"""
		Get profile
		Retrieve the properties and relationships of a profile object for a given user. The profile resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by profile.
		Find more info here: https://learn.microsoft.com/graph/api/profile-get?view=graph-rest-beta
		"""
		tags = ['me.profile']

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
		Update the navigation property profile in me
		
		"""
		tags = ['me.profile']

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
		Delete profile
		Delete a profile object from a user's account.
		Find more info here: https://learn.microsoft.com/graph/api/profile-delete?view=graph-rest-beta
		"""
		tags = ['me.profile']
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

	@property
	def account(self,
	) -> AccountRequest:
		from .account import AccountRequest
		return AccountRequest(self.request_adapter, self.path_parameters)

	@property
	def addresses(self,
	) -> AddressesRequest:
		from .addresses import AddressesRequest
		return AddressesRequest(self.request_adapter, self.path_parameters)

	@property
	def anniversaries(self,
	) -> AnniversariesRequest:
		from .anniversaries import AnniversariesRequest
		return AnniversariesRequest(self.request_adapter, self.path_parameters)

	@property
	def awards(self,
	) -> AwardsRequest:
		from .awards import AwardsRequest
		return AwardsRequest(self.request_adapter, self.path_parameters)

	@property
	def certifications(self,
	) -> CertificationsRequest:
		from .certifications import CertificationsRequest
		return CertificationsRequest(self.request_adapter, self.path_parameters)

	@property
	def educational_activities(self,
	) -> EducationalActivitiesRequest:
		from .educational_activities import EducationalActivitiesRequest
		return EducationalActivitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def emails(self,
	) -> EmailsRequest:
		from .emails import EmailsRequest
		return EmailsRequest(self.request_adapter, self.path_parameters)

	@property
	def interests(self,
	) -> InterestsRequest:
		from .interests import InterestsRequest
		return InterestsRequest(self.request_adapter, self.path_parameters)

	@property
	def languages(self,
	) -> LanguagesRequest:
		from .languages import LanguagesRequest
		return LanguagesRequest(self.request_adapter, self.path_parameters)

	@property
	def names(self,
	) -> NamesRequest:
		from .names import NamesRequest
		return NamesRequest(self.request_adapter, self.path_parameters)

	@property
	def notes(self,
	) -> NotesRequest:
		from .notes import NotesRequest
		return NotesRequest(self.request_adapter, self.path_parameters)

	@property
	def patents(self,
	) -> PatentsRequest:
		from .patents import PatentsRequest
		return PatentsRequest(self.request_adapter, self.path_parameters)

	@property
	def phones(self,
	) -> PhonesRequest:
		from .phones import PhonesRequest
		return PhonesRequest(self.request_adapter, self.path_parameters)

	@property
	def positions(self,
	) -> PositionsRequest:
		from .positions import PositionsRequest
		return PositionsRequest(self.request_adapter, self.path_parameters)

	@property
	def projects(self,
	) -> ProjectsRequest:
		from .projects import ProjectsRequest
		return ProjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def publications(self,
	) -> PublicationsRequest:
		from .publications import PublicationsRequest
		return PublicationsRequest(self.request_adapter, self.path_parameters)

	@property
	def skills(self,
	) -> SkillsRequest:
		from .skills import SkillsRequest
		return SkillsRequest(self.request_adapter, self.path_parameters)

	@property
	def web_accounts(self,
	) -> WebAccountsRequest:
		from .web_accounts import WebAccountsRequest
		return WebAccountsRequest(self.request_adapter, self.path_parameters)

	@property
	def websites(self,
	) -> WebsitesRequest:
		from .websites import WebsitesRequest
		return WebsitesRequest(self.request_adapter, self.path_parameters)

