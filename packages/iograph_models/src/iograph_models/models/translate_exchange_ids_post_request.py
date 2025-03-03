from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Translate_exchange_idsPostRequest(BaseModel):
	InputIds: Optional[list[str]] = Field(default=None,alias="InputIds",)
	TargetIdType: Optional[ExchangeIdFormat] = Field(default=None,alias="TargetIdType",)
	SourceIdType: Optional[ExchangeIdFormat] = Field(default=None,alias="SourceIdType",)

from .exchange_id_format import ExchangeIdFormat
from .exchange_id_format import ExchangeIdFormat

