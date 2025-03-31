from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Profile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.profile"] = Field(alias="@odata.type",)
	account: Optional[list[UserAccountInformation]] = Field(alias="account", default=None,)
	addresses: Optional[list[ItemAddress]] = Field(alias="addresses", default=None,)
	anniversaries: Optional[list[PersonAnnualEvent]] = Field(alias="anniversaries", default=None,)
	awards: Optional[list[PersonAward]] = Field(alias="awards", default=None,)
	certifications: Optional[list[PersonCertification]] = Field(alias="certifications", default=None,)
	educationalActivities: Optional[list[EducationalActivity]] = Field(alias="educationalActivities", default=None,)
	emails: Optional[list[ItemEmail]] = Field(alias="emails", default=None,)
	interests: Optional[list[PersonInterest]] = Field(alias="interests", default=None,)
	languages: Optional[list[LanguageProficiency]] = Field(alias="languages", default=None,)
	names: Optional[list[PersonName]] = Field(alias="names", default=None,)
	notes: Optional[list[PersonAnnotation]] = Field(alias="notes", default=None,)
	patents: Optional[list[ItemPatent]] = Field(alias="patents", default=None,)
	phones: Optional[list[ItemPhone]] = Field(alias="phones", default=None,)
	positions: Optional[list[WorkPosition]] = Field(alias="positions", default=None,)
	projects: Optional[list[ProjectParticipation]] = Field(alias="projects", default=None,)
	publications: Optional[list[ItemPublication]] = Field(alias="publications", default=None,)
	skills: Optional[list[SkillProficiency]] = Field(alias="skills", default=None,)
	webAccounts: Optional[list[WebAccount]] = Field(alias="webAccounts", default=None,)
	websites: Optional[list[PersonWebsite]] = Field(alias="websites", default=None,)

from .user_account_information import UserAccountInformation
from .item_address import ItemAddress
from .person_annual_event import PersonAnnualEvent
from .person_award import PersonAward
from .person_certification import PersonCertification
from .educational_activity import EducationalActivity
from .item_email import ItemEmail
from .person_interest import PersonInterest
from .language_proficiency import LanguageProficiency
from .person_name import PersonName
from .person_annotation import PersonAnnotation
from .item_patent import ItemPatent
from .item_phone import ItemPhone
from .work_position import WorkPosition
from .project_participation import ProjectParticipation
from .item_publication import ItemPublication
from .skill_proficiency import SkillProficiency
from .web_account import WebAccount
from .person_website import PersonWebsite
