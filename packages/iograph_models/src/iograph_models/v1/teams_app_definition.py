from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorization: Optional[TeamsAppAuthorization] = Field(alias="authorization",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publishingState: Optional[TeamsAppPublishingState | str] = Field(alias="publishingState",default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription",default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	bot: Optional[TeamworkBot] = Field(alias="bot",default=None,)

from .teams_app_authorization import TeamsAppAuthorization
from .identity_set import IdentitySet
from .teams_app_publishing_state import TeamsAppPublishingState
from .teamwork_bot import TeamworkBot

