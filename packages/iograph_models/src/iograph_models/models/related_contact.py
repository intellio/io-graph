from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RelatedContact(BaseModel):
	accessConsent: Optional[bool] = Field(default=None,alias="accessConsent",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	mobilePhone: Optional[str] = Field(default=None,alias="mobilePhone",)
	relationship: Optional[ContactRelationship] = Field(default=None,alias="relationship",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .contact_relationship import ContactRelationship

