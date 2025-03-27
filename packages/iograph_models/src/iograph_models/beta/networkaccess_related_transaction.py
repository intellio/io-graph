from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedTransaction(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedTransaction"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedTransaction")
	transactionId: Optional[str] = Field(alias="transactionId", default=None,)


