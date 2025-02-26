from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PublicationFacet(BaseModel):
	checkedOutBy: Optional[IdentitySet] = Field(default=None,alias="checkedOutBy",)
	level: Optional[str] = Field(default=None,alias="level",)
	versionId: Optional[str] = Field(default=None,alias="versionId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

