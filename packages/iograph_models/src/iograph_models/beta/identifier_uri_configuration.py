from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentifierUriConfiguration(BaseModel):
	nonDefaultUriAddition: Optional[IdentifierUriRestriction] = Field(alias="nonDefaultUriAddition",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identifier_uri_restriction import IdentifierUriRestriction

