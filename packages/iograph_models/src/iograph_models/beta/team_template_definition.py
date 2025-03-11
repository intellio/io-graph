from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamTemplateDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	audience: Optional[TeamTemplateAudience | str] = Field(alias="audience",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	iconUrl: Optional[str] = Field(alias="iconUrl",default=None,)
	languageTag: Optional[str] = Field(alias="languageTag",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	parentTemplateId: Optional[str] = Field(alias="parentTemplateId",default=None,)
	publisherName: Optional[str] = Field(alias="publisherName",default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription",default=None,)
	teamDefinition: Optional[Team] = Field(alias="teamDefinition",default=None,)

from .team_template_audience import TeamTemplateAudience
from .identity_set import IdentitySet
from .team import Team

