from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CertificateBasedAuthConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CertificateBasedAuthConfiguration] = Field(alias="value",)

from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration

