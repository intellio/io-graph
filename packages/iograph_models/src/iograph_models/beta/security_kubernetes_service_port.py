from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityKubernetesServicePort(BaseModel):
	appProtocol: Optional[str] = Field(alias="appProtocol", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	nodePort: Optional[int] = Field(alias="nodePort", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	protocol: Optional[SecurityContainerPortProtocol | str] = Field(alias="protocol", default=None,)
	targetPort: Optional[str] = Field(alias="targetPort", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_container_port_protocol import SecurityContainerPortProtocol
