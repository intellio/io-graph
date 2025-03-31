from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LearningContent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.learningContent"] = Field(alias="@odata.type",)
	additionalTags: Optional[list[str]] = Field(alias="additionalTags", default=None,)
	contentWebUrl: Optional[str] = Field(alias="contentWebUrl", default=None,)
	contributors: Optional[list[str]] = Field(alias="contributors", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	format: Optional[str] = Field(alias="format", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	isPremium: Optional[bool] = Field(alias="isPremium", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	level: Optional[Level | str] = Field(alias="level", default=None,)
	numberOfPages: Optional[int] = Field(alias="numberOfPages", default=None,)
	skillTags: Optional[list[str]] = Field(alias="skillTags", default=None,)
	sourceName: Optional[str] = Field(alias="sourceName", default=None,)
	thumbnailWebUrl: Optional[str] = Field(alias="thumbnailWebUrl", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)

from .level import Level
