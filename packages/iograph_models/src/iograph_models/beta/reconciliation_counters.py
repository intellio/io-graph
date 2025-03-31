from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReconciliationCounters(BaseModel):
	user: Optional[ReconciliationCounter] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reconciliation_counter import ReconciliationCounter
