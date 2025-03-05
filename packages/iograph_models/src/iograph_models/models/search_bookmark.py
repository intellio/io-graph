from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SearchBookmark(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: Optional[SearchIdentitySet] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	availabilityEndDateTime: Optional[datetime] = Field(alias="availabilityEndDateTime",default=None,)
	availabilityStartDateTime: Optional[datetime] = Field(alias="availabilityStartDateTime",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	groupIds: Optional[list[str]] = Field(alias="groupIds",default=None,)
	isSuggested: Optional[bool] = Field(alias="isSuggested",default=None,)
	keywords: Optional[SearchAnswerKeyword] = Field(alias="keywords",default=None,)
	languageTags: Optional[list[str]] = Field(alias="languageTags",default=None,)
	platforms: Optional[list[str | DevicePlatformType]] = Field(alias="platforms",default=None,)
	powerAppIds: Optional[list[str]] = Field(alias="powerAppIds",default=None,)
	state: Optional[str | SearchAnswerState] = Field(alias="state",default=None,)
	targetedVariations: Optional[list[SearchAnswerVariant]] = Field(alias="targetedVariations",default=None,)

from .search_identity_set import SearchIdentitySet
from .search_answer_keyword import SearchAnswerKeyword
from .device_platform_type import DevicePlatformType
from .search_answer_state import SearchAnswerState
from .search_answer_variant import SearchAnswerVariant

