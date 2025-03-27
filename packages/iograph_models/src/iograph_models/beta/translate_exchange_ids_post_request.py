from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Translate_exchange_idsPostRequest(BaseModel):
	InputIds: Optional[list[str]] = Field(alias="InputIds", default=None,)
	TargetIdType: Optional[ExchangeIdFormat | str] = Field(alias="TargetIdType", default=None,)
	SourceIdType: Optional[ExchangeIdFormat | str] = Field(alias="SourceIdType", default=None,)

from .exchange_id_format import ExchangeIdFormat
from .exchange_id_format import ExchangeIdFormat

