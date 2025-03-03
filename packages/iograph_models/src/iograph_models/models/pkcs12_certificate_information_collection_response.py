from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Pkcs12CertificateInformationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Pkcs12CertificateInformation]] = Field(default=None,alias="value",)

from .pkcs12_certificate_information import Pkcs12CertificateInformation

