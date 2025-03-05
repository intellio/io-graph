from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SharingDetail(BaseModel):
	sharedBy: Optional[InsightIdentity] = Field(default=None,alias="sharedBy",)
	sharedDateTime: Optional[datetime] = Field(default=None,alias="sharedDateTime",)
	sharingReference: Optional[ResourceReference] = Field(default=None,alias="sharingReference",)
	sharingSubject: Optional[str] = Field(default=None,alias="sharingSubject",)
	sharingType: Optional[str] = Field(default=None,alias="sharingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .insight_identity import InsightIdentity
from .resource_reference import ResourceReference

