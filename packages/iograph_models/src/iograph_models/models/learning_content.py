from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LearningContent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalTags: Optional[list[str]] = Field(default=None,alias="additionalTags",)
	contentWebUrl: Optional[str] = Field(default=None,alias="contentWebUrl",)
	contributors: Optional[list[str]] = Field(default=None,alias="contributors",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	duration: Optional[str] = Field(default=None,alias="duration",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	format: Optional[str] = Field(default=None,alias="format",)
	isActive: Optional[bool] = Field(default=None,alias="isActive",)
	isPremium: Optional[bool] = Field(default=None,alias="isPremium",)
	isSearchable: Optional[bool] = Field(default=None,alias="isSearchable",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	level: Optional[Level] = Field(default=None,alias="level",)
	numberOfPages: Optional[int] = Field(default=None,alias="numberOfPages",)
	skillTags: Optional[list[str]] = Field(default=None,alias="skillTags",)
	sourceName: Optional[str] = Field(default=None,alias="sourceName",)
	thumbnailWebUrl: Optional[str] = Field(default=None,alias="thumbnailWebUrl",)
	title: Optional[str] = Field(default=None,alias="title",)

from .level import Level

