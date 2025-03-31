from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RelatedPerson(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	relationship: Optional[PersonRelationship | str] = Field(alias="relationship", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .person_relationship import PersonRelationship
