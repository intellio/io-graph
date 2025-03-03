from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SearchQna(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[SearchIdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	availabilityEndDateTime: Optional[datetime] = Field(default=None,alias="availabilityEndDateTime",)
	availabilityStartDateTime: Optional[datetime] = Field(default=None,alias="availabilityStartDateTime",)
	groupIds: Optional[list[str]] = Field(default=None,alias="groupIds",)
	isSuggested: Optional[bool] = Field(default=None,alias="isSuggested",)
	keywords: Optional[SearchAnswerKeyword] = Field(default=None,alias="keywords",)
	languageTags: Optional[list[str]] = Field(default=None,alias="languageTags",)
	platforms: Optional[list[DevicePlatformType]] = Field(default=None,alias="platforms",)
	state: Optional[SearchAnswerState] = Field(default=None,alias="state",)
	targetedVariations: Optional[list[SearchAnswerVariant]] = Field(default=None,alias="targetedVariations",)

from .search_identity_set import SearchIdentitySet
from .search_answer_keyword import SearchAnswerKeyword
from .device_platform_type import DevicePlatformType
from .search_answer_state import SearchAnswerState
from .search_answer_variant import SearchAnswerVariant

