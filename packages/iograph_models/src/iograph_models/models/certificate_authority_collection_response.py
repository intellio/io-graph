from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CertificateAuthorityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CertificateAuthority]] = Field(default=None,alias="value",)

from .certificate_authority import CertificateAuthority

