from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesServicePortCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityKubernetesServicePort]] = Field(alias="value", default=None,)

from .security_kubernetes_service_port import SecurityKubernetesServicePort

