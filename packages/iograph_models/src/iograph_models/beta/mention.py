from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Mention(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mention"] = Field(alias="@odata.type",)
	application: Optional[str] = Field(alias="application", default=None,)
	clientReference: Optional[str] = Field(alias="clientReference", default=None,)
	createdBy: Optional[Union[TypedEmailAddress]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deepLink: Optional[str] = Field(alias="deepLink", default=None,)
	mentioned: Optional[Union[TypedEmailAddress]] = Field(alias="mentioned", default=None,discriminator="odata_type", )
	mentionText: Optional[str] = Field(alias="mentionText", default=None,)
	serverCreatedDateTime: Optional[datetime] = Field(alias="serverCreatedDateTime", default=None,)

from .typed_email_address import TypedEmailAddress
