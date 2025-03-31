from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomAppManagementApplicationConfiguration(BaseModel):
	identifierUris: Optional[IdentifierUriConfiguration] = Field(alias="identifierUris", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .identifier_uri_configuration import IdentifierUriConfiguration
