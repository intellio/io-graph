from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedIdentity(BaseModel):
	associatedResourceId: Optional[str] = Field(alias="associatedResourceId",default=None,)
	federatedTokenId: Optional[str] = Field(alias="federatedTokenId",default=None,)
	federatedTokenIssuer: Optional[str] = Field(alias="federatedTokenIssuer",default=None,)
	msiType: Optional[MsiType | str] = Field(alias="msiType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .msi_type import MsiType

