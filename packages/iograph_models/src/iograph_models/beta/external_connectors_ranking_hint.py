from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsRankingHint(BaseModel):
	importanceScore: Optional[ExternalConnectorsImportanceScore | str] = Field(alias="importanceScore", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_connectors_importance_score import ExternalConnectorsImportanceScore
