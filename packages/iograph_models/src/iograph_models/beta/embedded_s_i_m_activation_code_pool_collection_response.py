from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmbeddedSIMActivationCodePoolCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[EmbeddedSIMActivationCodePool]] = Field(alias="value",default=None,)

from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool

