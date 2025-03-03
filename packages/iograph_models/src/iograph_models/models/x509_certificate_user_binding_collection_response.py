from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateUserBindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[X509CertificateUserBinding]] = Field(default=None,alias="value",)

from .x509_certificate_user_binding import X509CertificateUserBinding

