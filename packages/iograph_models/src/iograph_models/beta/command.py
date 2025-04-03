from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Command(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.command"] = Field(alias="@odata.type", default="#microsoft.graph.command")
	appServiceName: Optional[str] = Field(alias="appServiceName", default=None,)
	error: Optional[str] = Field(alias="error", default=None,)
	packageFamilyName: Optional[str] = Field(alias="packageFamilyName", default=None,)
	payload: Optional[PayloadRequest] = Field(alias="payload", default=None,)
	permissionTicket: Optional[str] = Field(alias="permissionTicket", default=None,)
	postBackUri: Optional[str] = Field(alias="postBackUri", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	responsepayload: Optional[PayloadResponse] = Field(alias="responsepayload", default=None,)

from .payload_request import PayloadRequest
from .payload_response import PayloadResponse
