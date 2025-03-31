from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ClientCertificateAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.clientCertificateAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.clientCertificateAuthentication")
	certificateList: Optional[list[Pkcs12CertificateInformation]] = Field(alias="certificateList", default=None,)

from .pkcs12_certificate_information import Pkcs12CertificateInformation
