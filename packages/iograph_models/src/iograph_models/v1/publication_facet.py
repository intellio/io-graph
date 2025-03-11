from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PublicationFacet(BaseModel):
	checkedOutBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="checkedOutBy",default=None,)
	level: Optional[str] = Field(alias="level",default=None,)
	versionId: Optional[str] = Field(alias="versionId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

