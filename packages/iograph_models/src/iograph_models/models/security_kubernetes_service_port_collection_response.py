from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesServicePortCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityKubernetesServicePort]] = Field(default=None,alias="value",)

from .security_kubernetes_service_port import SecurityKubernetesServicePort

