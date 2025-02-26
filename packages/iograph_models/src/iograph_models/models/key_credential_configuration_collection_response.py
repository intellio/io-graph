from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class KeyCredentialConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[KeyCredentialConfiguration] = Field(alias="value",)

from .key_credential_configuration import KeyCredentialConfiguration

