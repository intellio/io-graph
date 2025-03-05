from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemVersion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publication: Optional[PublicationFacet] = Field(alias="publication",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)

from .identity_set import IdentitySet
from .publication_facet import PublicationFacet

