from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authorization: Optional[TeamsAppAuthorization] = Field(default=None,alias="authorization",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publishingState: Optional[TeamsAppPublishingState] = Field(default=None,alias="publishingState",)
	shortDescription: Optional[str] = Field(default=None,alias="shortDescription",)
	teamsAppId: Optional[str] = Field(default=None,alias="teamsAppId",)
	version: Optional[str] = Field(default=None,alias="version",)
	bot: Optional[TeamworkBot] = Field(default=None,alias="bot",)

from .teams_app_authorization import TeamsAppAuthorization
from .identity_set import IdentitySet
from .teams_app_publishing_state import TeamsAppPublishingState
from .teamwork_bot import TeamworkBot

