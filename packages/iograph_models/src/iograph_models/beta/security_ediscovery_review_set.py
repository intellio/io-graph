from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryReviewSet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	files: Optional[list[SecurityEdiscoveryFile]] = Field(alias="files",default=None,)
	queries: Optional[list[SecurityEdiscoveryReviewSetQuery]] = Field(alias="queries",default=None,)

from .identity_set import IdentitySet
from .security_ediscovery_file import SecurityEdiscoveryFile
from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

