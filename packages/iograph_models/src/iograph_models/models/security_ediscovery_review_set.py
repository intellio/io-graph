from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoveryReviewSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	queries: Optional[list[SecurityEdiscoveryReviewSetQuery]] = Field(default=None,alias="queries",)

from .identity_set import IdentitySet
from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

