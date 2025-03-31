from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SamlOrWsFedExternalDomainFederationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SamlOrWsFedExternalDomainFederation]] = Field(alias="value", default=None,)

from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
