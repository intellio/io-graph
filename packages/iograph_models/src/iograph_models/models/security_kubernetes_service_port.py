from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesServicePort(BaseModel):
	appProtocol: Optional[str] = Field(default=None,alias="appProtocol",)
	name: Optional[str] = Field(default=None,alias="name",)
	nodePort: Optional[int] = Field(default=None,alias="nodePort",)
	port: Optional[int] = Field(default=None,alias="port",)
	protocol: Optional[SecurityContainerPortProtocol] = Field(default=None,alias="protocol",)
	targetPort: Optional[str] = Field(default=None,alias="targetPort",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_container_port_protocol import SecurityContainerPortProtocol

