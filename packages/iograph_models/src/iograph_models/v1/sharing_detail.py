from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharingDetail(BaseModel):
	sharedBy: Optional[InsightIdentity] = Field(alias="sharedBy", default=None,)
	sharedDateTime: Optional[datetime] = Field(alias="sharedDateTime", default=None,)
	sharingReference: Optional[ResourceReference] = Field(alias="sharingReference", default=None,)
	sharingSubject: Optional[str] = Field(alias="sharingSubject", default=None,)
	sharingType: Optional[str] = Field(alias="sharingType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .insight_identity import InsightIdentity
from .resource_reference import ResourceReference
