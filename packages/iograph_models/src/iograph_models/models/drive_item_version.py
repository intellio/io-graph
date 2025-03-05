from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemVersion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publication: Optional[PublicationFacet] = Field(default=None,alias="publication",)
	content: Optional[str] = Field(default=None,alias="content",)
	size: Optional[int] = Field(default=None,alias="size",)

from .identity_set import IdentitySet
from .publication_facet import PublicationFacet

