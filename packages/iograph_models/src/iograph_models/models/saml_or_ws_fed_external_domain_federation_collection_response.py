from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SamlOrWsFedExternalDomainFederationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SamlOrWsFedExternalDomainFederation]] = Field(default=None,alias="value",)

from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

