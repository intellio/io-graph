from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RelatedContact(BaseModel):
	accessConsent: Optional[bool] = Field(alias="accessConsent", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	mobilePhone: Optional[str] = Field(alias="mobilePhone", default=None,)
	relationship: Optional[ContactRelationship | str] = Field(alias="relationship", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .contact_relationship import ContactRelationship

